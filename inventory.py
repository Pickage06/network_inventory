#!/usr/bin/env python3
# coding: utf-8
import nmap3
import os
import arpreq
import requests
import json
import csv
import pymysql.cursors
import sys

######## INVENTORY HARDWARE ########
"""The objective of the script is to make an inventory
of all the equipments on a factory. To do that, please observe 
the following instructions  """

### 1 ### Find IP Address ###
# Do a nmap in your subnet #
def nmap():
  nm = nmap3.Nmap()
  result = nm.nmap_subnet_scan(sys.argv[1])
  # Stock IPs in a global variable tu use it below #
  global ips
  ips=list(result.keys())[:-2] # without results "stats" and "runtime" #
  
# Call nmap fonction #
nmap()

### 2 ### Create a dictionnary to stock futur elements ###
resultat = {}

### 3 ### Find MAC Address ###
def arping(): 
# For each ip do an arping #
  for ip in ips:
    # Create a variable mac to stock each mac address # 
    mac = arpreq.arpreq(ip)
    # Stock each result of ip and mac in a dictionnary #
    resultat[ip] = mac

# Call arping fonction #
arping() 

### 4 ### Find API Constructor ###
"""With resultat{ip,mac} ask to the api constructor's informations"""
def vendor():
  for ip_dic,mac_liste in resultat.items():
    # Create a variable to insert the correct mac adress in the url#
    url_api = "http://www.macvendorlookup.com/api/v2/{"+ mac_liste +"}"
    # Obtain the result of the API Rest #
    response_api = requests.get(url_api)
    # Transform the response API in json format #
    response_json = response_api.json()
    # Extract the list in the json's dictionnary #
    dic = response_json[0]
    # Look after the company's equipment in the json's result #
    # Stock informations to complete values in the dictionnary "resultat" #
    resultat[ip_dic] = [mac_liste,dic["company"]] 
    
# Call the vendor's fonction # 
vendor()

### 5 ### Transfer the dictionnary "resultat" on a database ###
# Open database connection #
connection = pymysql.connect(host='localhost',
                              user='antho',
                              password='',
                              database='inventory',
                              cursorclass=pymysql.cursors.DictCursor)

def mysql():
  with connection:
    with connection.cursor() as cursor:
      # Ask to clean the table "inventaire" #
      cursor.execute("TRUNCATE TABLE inventory.inventaire")

      # Create a loop to add any items of the dictionnary "resultat" into a list "final" #
      for key,value in resultat.items():
        final = []
        final.append(key)
        for each_value in value:
          final.append(each_value)

        # Create a variable will be use for the sql request instead of "VALUES" #
        data = ""
        # For each element in my variable, add them #
        for element in final:
          data += "'" + element + "'" + ","

        # Building of the SQL requests
        data_sql = data.rstrip(",")
        # Insert into table "inventaire SQL request"
        add_value = f"INSERT INTO inventaire VALUES({data_sql});"

        # Execute the SQL request #
        cursor.execute(add_value)
        connection.commit()	

# Call mysql fonction #
mysql()

# Close the SQL connection #
cursor.close()
connection.close()
