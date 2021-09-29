# Network_Inventory

# This project is expected to look after what devices are switch on, to recover their IP address, MAC address too and ask with the api constructor some information. 

#FOR BEGINNING

First, you need to know how use nmap, arping and how ask api constructor
First, you need to know manipulate lists, dictionnarys and variables' pyhton
Explication: 

Nmap is a modul use to search on the network informations about devices switch on. Informations like IP address. 

Arping is a modul use to check about the Mac address by supplying IP address

API constructor is an Application Programming Interface, create by the constructor to permit access everyone at some informations. Like the company of the device, date, version of the equipment etc.  


#PREREQUISITE

Nmap.nmap()
arpreq.arpreq(ip)
http://www.macvendorlookup.com/api/v2/{"+ MAC_Address +"}


#INSTALLATION

To realise the execution of this script, you may execute some tasks:

1- Search about the IP address by using nmap modul (def nmap():)

1.2- Extract IPs addresses on the result's dictionnary (IPs will be keys of the dictionnary)

2- Create a dictionnary to stock IPs (IPs will be keys of the dictionnary again)

3- Use IPs to make an arping (need only one IP for working, do a loop) and obtain MAC addresses (def arping():)

3.2- Stock each MAC address with the respective IP address on the dictionnary created on step "2".

4- Use MAC Address to ask API vendor's informations and stock them on the dictionnary on step "2"

5- Save all informations of the dictionnary on a csv file (def save_file():)

You will obtain results as file.csv, this file will be save in the same directory as the script 

#ADAPTATION
To adpate the script with your own network, please change the subnet on the line 20. 

#STARTING
To start the script, verify if the subnet had been changed by your own subnet. 
Verify if the script can be executed (else: chmod +x file.py)


#TO GO FURTHER

If you want traduce your resultat on website, thanks to follow the instructions bellow: 

Install phpmyadmin
Install mysql
This is the config file for phpmyadmin

This is the config file for mysql


BUILT WITH Guillaume DUALE
https://github.com/tazou


VERSIONS 
version 1.0

AUTORS
Anthony LANIESSE : anlaniessepro@gmail.com
Guillaume DUALE

LICENCE
This project is available under GNU General Public License v3.0
