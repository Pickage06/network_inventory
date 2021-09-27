#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import nmap3
import os
import arpreq
import requests
import json
import csv

######## INVENTORY HARDWARE ########
"""The objective of the script is to make an inventory
of all the equipments on a factory. To do that, please observe 
the following instructions  """


###Find IP Address###
#Do a nmap in your subnet#
def nmap():
  nm = nmap3.Nmap()
  result = nm.nmap_subnet_scan("192.168.172.0/24")
  #Stock IPs in a variable tu use it below#
  global ips
  ips=list(result.keys())[:-2]#"""without the result stats and runtime"""
  
#Call nmap fonction#
nmap()

#Create a dictionnary to stock futur elements#
resultat = {}

###Find MAC Address###
def arping(): 
#For each ip do an arping#
  for ip in ips:
#Create a variable mac to recover each mac address#
    mac = arpreq.arpreq(ip)
#Stock each result of ip and mac in a dictionnary#
    resultat[ip] = mac

#Call arping fonction#
arping() 

###Find API Constructor###
"""With the list ask to the api constructor's informations"""
def vendor():
  for ip_dic,mac_liste in resultat.items():
#Create a variable to insert the correct mac adress on the url#
    url_api = "http://www.macvendorlookup.com/api/v2/{"+ mac_liste +"}"
#Obtain the result of the API Rest#
    response_api = requests.get(url_api)
#Transform the response APi in json format#
    response_json = response_api.json()
#Extract the list on the json's dictionnary#     
    dic = response_json[0]
#Look after the company's equipment in the json's result#
#Stock informations to complete values in the dictionnary "resultat"#
    resultat[ip_dic] = [mac_liste,dic["company"]] 
    
#Call the vendor's fonction# 
vendor()

#Save the dictionnary on a csv file#
with open('resultat.csv','w') as fichiercsv:
  writer = csv.writer(fichiercsv)
#For each items in my dictionnary, save it#
  for key,value in resultat.items():
    writer.writerow([key,value])

print(resultat)
