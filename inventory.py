#!/usr/bin/env python3
# coding: utf-8
import nmap3
import os
import arpreq
import requests
import json
import csv
import pymysql.cursors

######## INVENTORY HARDWARE ########
"""The objective of the script is to make an inventory
of all the equipments on a factory. To do that, please observe 
the following instructions  """


### Find IP Address ###
# Do a nmap in your subnet #
def nmap():
  nm = nmap3.Nmap()
  result = nm.nmap_subnet_scan("192.168.172.0/24")
  # Stock IPs in a variable tu use it below #
  global ips
  ips=list(result.keys())[:-2] # without results "stats" and "runtime" #
  
# Call nmap fonction #
nmap()

# Create a dictionnary to stock futur elements #
resultat = {}


### Find MAC Address ###
def arping(): 
# For each ip do an arping #
  for ip in ips:
    # Create a variable mac to stock each mac address # 
    mac = arpreq.arpreq(ip)
    # Stock each result of ip and mac in a dictionnary #
    resultat[ip] = mac

# Call arping fonction #
arping() 


### Find API Constructor ###
"""With resultat{ip,mac} ask to the api constructor's informations"""
def vendor():
  for ip_dic,mac_liste in resultat.items():
    # Create a variable to insert the correct mac adress on the url#
    url_api = "http://www.macvendorlookup.com/api/v2/{"+ mac_liste +"}"
    # Obtain the result of the API Rest #
    response_api = requests.get(url_api)
    # Transform the response APi in json format #
    response_json = response_api.json()
    # Extract the list on the json's dictionnary #
    dic = response_json[0]
    # Look after the company's equipment in the json's result #
    # Stock informations to complete values in the dictionnary "resultat" #
    resultat[ip_dic] = [mac_liste,dic["company"]] 
    
# Call the vendor's fonction # 
vendor()

### Transfer the dictionnary "resultat" on a database ###
# Open database connection #
connection = pymysql.connect(host='localhost',
                              user='antho',
                              password='hello',
                              database='inventory',
                              cursorclass=pymysql.cursors.DictCursor)


def mysql():
  with connection:
    with connection.cursor() as cursor:

      # On créé la même boucle que l'on avait utilisé pour écrire dans le fichier csv.
      for key,value in resultat.items():
        l = []
        l.append(key)
        for e in value:
          l.append(e)
        print(l)

        # On construit la partie qui sera utilisé après le "VALUES" dans la requête SQL.
        donnee = ""
        for element in l:
          donnee += "'" + element + "'" + ","

        # Construction de la requête SQL
        print(donnee)
        donnee_sql = donnee.rstrip(",")
        print(donnee_sql)
        add_value = f"INSERT INTO inventaire VALUES({donnee_sql});"
        print(add_value)

        # Execution de la requête SQL
        cursor.execute(add_value)
        connection.commit()

        #placeholders = ', '.join(['%s'] * len(resultat))
        #columns = ', '.join("`" + str(x).replace('/', '_') + "`" for x in resultat.keys())
        #values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in list(resultat.values()))
        #add_value = """INSERT INTO inventaire ( %s ) VALUES ( %s )""" % (columns, values)
        #print(add_value)
        #cursor.execute(add_value, list(resultat.values()))
        #cursor.execute(add_value)
        #connection.commit()
        #print(add_value)

#columns = ', '.join("`" + str(x).replace('/', '_') + "`" for x in resulat.keys())
#values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in mydict.values())
#sql = "INSERT INTO %s ( %s ) VALUES ( %s );" % ('mytable', columns, values)


mysql()
