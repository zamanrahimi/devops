<h2>Version: v2.18</h2>
<?php
$servername = "mysql-service";  // The name of the MySQL service in your Kubernetes cluster
$username = "root";
$password = "";
$database = "db2";
$port = 3306;

// Create connection
$conn = new mysqli($servername, $username, $password, $database, $port);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

echo "Connected successfully";

// Perform your database operations here

// Fetch data from the "empt" table
$sql = "SELECT id, name FROM empt";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    // Output data of each row
    echo "<ul>";
    while($row = $result->fetch_assoc()) {
        echo "<li>IDs: " . $row["id"]. " - Name: " . $row["name"]. "</li>";
    }
    echo "</ul>";
} else {
    echo "No records found";
}

$conn->close();
?>
