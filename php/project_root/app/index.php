<?php
$host = 'db';  // This is the service name of your MySQL container
$db = 'energytransfer';
$user = 'root';  // Replace with your MySQL username
$pass = 'admin';  // Replace with your MySQL password

// Create a connection
$conn = new mysqli($host, $user, $pass, $db);

// Check the connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

echo "Connected to MySQL successfully!";

// Close the connection
$conn->close();
?>
