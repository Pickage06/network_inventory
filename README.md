# Network Inventory

ce logiciel est utilisé pour inventorié les equipements réseaux actifs
Il stock cet inventaire dans une base de donnée sql

In more details,this project is expected to look after what devices are switch on, to recover their IP address, MAC address too and ask with the api constructor some information.
 
## FOR BEGINNING

That you need to know : 

First, you need to know manipulate lists, dictionnarys and variables' Pyhton.

In a second time, you need to know how use nmap, arping and how ask api constructor.

For finish, you need to use mysql to stock results on a database.

Explanations:

Nmap is a module used to search on the network some informations about devices switch on. Informations like IP address. 

Arping is a module used to check about the Mac address by supplying IP address.

API constructor is an Application Programming Interface, created by the constructor to permit access everyone at some informations. Like the company of the device, date, version of the equipment etc.  

Mysql is a Database Management System(DBMS)  which stock informations.

### PREREQUISITE

- Install mysql.

> sudo apt install -y mysql-server

- Create a database mysql.

> mysql> create database inventory;

- Create an user mysql with password.

> mysql> CREATE USER 'app'@'localhost' IDENTIFIED BY 'azerty';

- Give privileges to your user.

> mysql> GRANT ALL PRIVILEGES ON inventory.* TO 'app'@'localhost';

- Create a table to stock informations.

> mysql> create database database_name;

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
To adpate the script with your own network, please just indicate your subnet following the execution of the script (example: .inventory.py 192.168.172.0/24) 

Change the bloc of sql connection between line 67 at 70 with your own access.

## STARTING
To start the script, verify if the subnet had been changed by your own subnet (respect the line 68 of "Adaptation")
Verify if the script can be executed (else: chmod +x inventory.py)

### TO GO FURTHER
If you want traduce your result on website, thanks to follow the instructions bellow: 

Install apache-server.

sudo apt install -y apache2

sudo apt install -y libapache2-mod-php

This is the config of [index.php](index.php) (var/www/html/index.php):

## VERSIONS
Version 1.0

## AUTORS
Anthony LANIESSE : anlaniessepro@gmail.com
[Guillaume DUALE](https://github.com/tazou)

## LICENCE
This project is available under GNU General Public License v3.0 - see the file [LICENSE](LICENSE) for more informations.

