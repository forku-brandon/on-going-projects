<?php
session_start();

// Retrieve the value from the PHP session variable
$phpVariable = $_SESSION['phpVariable'];

// Perform any desired operations with the PHP variable
echo "Value received from JavaScript: " . $phpVariable;
?>

