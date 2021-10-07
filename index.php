<?php

echo "<h1>Welcome on my inventory network</h1>";

$servername = "localhost";
$username = "antho";
$password = "hello";
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
    echo "ip " . $row["ip"]. " - Mac: " . $row["mac"]. " Company " . $row["vendor"]. "<br>";
  }
} else {
  echo "0 results";
}
$conn->close();

?>
