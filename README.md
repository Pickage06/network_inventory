# Network Inventory
This software is used to make an inventory of active network equipments.

It stock this inventory on a SQL database.

In more details, this project is expected to look after what devices are switch on, to recover their IP address, MAC address too and ask with the api constructor some information.

Explanations:

Nmap is a module used to search on the network some informations about devices switch on. Informations like IP address. 

Arping is a module used to check about the Mac address by supplying IP address.

API constructor is an Application Programming Interface, created by the constructor to permit access everyone at some informations. Like the company of the device, date, version of the equipment etc.  

Mysql is a Database Management System(DBMS)  which stock informations.

## PREREQUISITE

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

- Install Python dependencies

> pip3 install -r requierements.txt

- Mysql credential

Change the bloc of SQL connection between line 67 at 70 with your own informations.

- Verify if the script can be executed (else: chmod +x inventory.py)

## HOW TO USE IT
> ./inventory.py your_subnet

_exemple :_ > ./inventory.py 192.168.172.0/24

## HOW MY SOFTWARE WORKS
To realise the execution of this script, you may execute some tasks:

1- Search about the IP address by using nmap modul "def nmap():".

1.2- Extract IPs addresses on the result, it is a dictionnary (IPs are keys of the dictionnary)

2- Create a dictionnary to stock informations

3- Use IPs to make an arping (need only one IP for working, do a loop) and obtain MAC addresses "def arping():".

3.2- Stock each MAC address with the respective IP address on the dictionnary created on step "2".

4- Use MAC Address to ask API vendor's informations and stock them on the dictionnary on step "2"

5- Use dictionnary "resultat" to make a SQL requests and stocks informations on a database "def mysql():".

## TO GO FURTHER
If you want display your result on website, thanks to follow the instructions bellow: 

Install apache-server.

> sudo apt install -y apache2 libapache2-mod-php php-mysql

Copy the file [index.php](index.php) in the directory /var/www/html/

Don't forget to adapt your login access between line 5 to 8 in the index.php file.

## VERSIONS
Version 1.0

## AUTORS
Anthony LANIESSE : anlaniessepro@gmail.com

[Guillaume DUALE](https://github.com/tazou)

## LICENCE
This project is available under GNU General Public License v3.0 - see the file [LICENSE](LICENSE) for more informations.

