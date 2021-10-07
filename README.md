# Network Inventory

This project is expected to look after what devices are switch on, to recover their IP address, MAC address too and ask with the api constructor some information. 

## FOR BEGINNING
First, you need to know manipulate lists, dictionnarys and variables' pyhton.

In a second time, you need to know how use nmap, arping and how ask api constructor.

For finish, you need to use mysql to stock results on a database.
Explication: 

Nmap is a modul use to search on the network some informations about devices switch on. Informations like IP address. 

Arping is a modul use to check about the Mac address by supplying IP address.

API constructor is an Application Programming Interface, create by the constructor to permit access everyone at some informations. Like the company of the device, date, version of the equipment etc.  

Mysql is a software which stock informations, in databases.

### PREREQUISITE
Nmap.nmap()

arpreq.arpreq(ip)

http://www.macvendorlookup.com/api/v2/{"+ MAC_Address +"}

If you want save your information on a database, thanks to follow this instructions first:

1- Install mysql.

sudo apt install -y mysql-server

2- Create a database mysql.

mysql> create database inventory;

3- Create an user mysql with password.

mysql> CREATE USER 'app'@'localhost' IDENTIFIED BY 'azerty';

4- Give privileges to your user.

mysql> GRANT ALL PRIVILEGES ON inventory. TO 'app'@'localhost';

5- Create a table to stock informations.

mysql> create database database_name;

### INSTALLATION
To realise the execution of this script, you may execute some tasks:

1- Search about the IP address by using nmap modul "def nmap():".

1.2- Extract IPs addresses on the result, it is a dictionnary (IPs are keys of the dictionnary)

2- Create a dictionnary to stock informations

3- Use IPs to make an arping (need only one IP for working, do a loop) and obtain MAC addresses "def arping():".

3.2- Stock each MAC address with the respective IP address on the dictionnary created on step "2".

4- Use MAC Address to ask API vendor's informations and stock them on the dictionnary on step "2"

5- Use dictionnary "resultat" to make a SQL requests and stocks informations on a database "def mysql():".

## ADAPTATION
To adpate the script with your own network, please change the subnet on the line 20. 

Change the bloc of sql connection between line 67 at 70 with your own access.

## STARTING
To start the script, verify if the subnet had been changed by your own subnet. 
Verify if the script can be executed (else: chmod +x file.py)

### TO GO FURTHER
If you want traduce your resultat on website, thanks to follow the instructions bellow: 

Install apache-server.

sudo apt install -y apache2

sudo apt install -y libapache2-mod-php

This is the config php file (var/www/html/index.php):

## BUILT WITH
[Guillaume DUALE](https://github.com/tazou)

## VERSIONS
Version 1.0

## AUTORS
Anthony LANIESSE : anlaniessepro@gmail.com
Guillaume DUALE

## LICENCE
This project is available under GNU General Public License v3.0 - see the file [LICENSE](LICENSE) for more informations.

