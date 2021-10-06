# Network Inventory

This project is expected to look after what devices are switch on, to recover their IP address, MAC address too and ask with the api constructor some information. 

## FOR BEGINNING

First, you need to know how use nmap, arping and how ask api constructor
First, you need to know manipulate lists, dictionnarys and variables' pyhton
Explication: 

Nmap is a modul use to search on the network informations about devices switch on. Informations like IP address. 

Arping is a modul use to check about the Mac address by supplying IP address

API constructor is an Application Programming Interface, create by the constructor to permit access everyone at some informations. Like the company of the device, date, version of the equipment etc.  


### PREREQUISITE

Nmap.nmap()
arpreq.arpreq(ip)
http://www.macvendorlookup.com/api/v2/{"+ MAC_Address +"}
mysql


### INSTALLATION

To realise the execution of this script, you may execute some tasks:

1- Search about the IP address by using nmap modul (def nmap():)

1.2- Extract IPs addresses on the result's dictionnary (IPs are keys of the dictionnary)

2- Create a dictionnary to stock informations

3- Use IPs to make an arping (need only one IP for working, do a loop) and obtain MAC addresses (def arping():)

3.2- Stock each MAC address with the respective IP address on the dictionnary created on step "2".

4- Use MAC Address to ask API vendor's informations and stock them on the dictionnary on step "2"

5- Use dictionnary "resultat" to make a SQL requests and stocks informations on a database (def mysql():)

## ADAPTATION
To adpate the script with your own network, please change the subnet on the line 20. 

## STARTING
To start the script, verify if the subnet had been changed by your own subnet. 
Verify if the script can be executed (else: chmod +x file.py)

### TO GO FURTHER

If you want traduce your resultat on website, thanks to follow the instructions bellow: 

Install apache-server
This is the config php file (var/www/html/index.php):
<?php
 
echo "<h1>Welcome on my inventory network</h1>";
 
$servername = "localhost";
$username = "antho";
$password = "";
$dbname = "inventory";
 
// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}
 
$sql = "SELECT * from inventaire;";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
  // output data of each row
  while($row = $result->fetch_assoc()) {
    echo "ip " . $row["ip"]. " - Mac: " . $row["mac"]. " Company " . $row["    vendor"]. "<br>";
  }
} else {
  echo "0 results";
}
$conn->close();
 
?>

This is the config file for mysql
How to created a 


## BUILT WITH Guillaume DUALE
https://github.com/tazou


## VERSIONS 
version 1.0

## AUTORS
Anthony LANIESSE : anlaniessepro@gmail.com
Guillaume DUALE

## LICENCE
This project is available under GNU General Public License v3.0
