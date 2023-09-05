

<?php


$target = "";
$Err = "";
if ($_SERVER["REQUEST_METHOD"] == "POST") {
  if (empty($_POST["name"])) {
    $Err= "Name is required";
  } else {
    $target = test_input($_POST["name"]);
  }}


function test_input($data)
{
  $data = trim($data);
  $data = stripslashes($data);
  $data = htmlspecialchars($data);
  return $data;
}


?>




<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>input</title>
</head>
<body>
<form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>">

        <input type="text" value="text"  name="name">
        <br><br><br>
        <input type="submit" value="search">
    </form>
    <div>
    <span class="error"> <?php echo $Err; ?></span>
    </div>
</body>
</html>




<?php

function searchWebPages($target, $url) {
    $html = file_get_contents($url); // Fetch the HTML content of the web page
    $matches = [];
    
    // Extract the desired values using regular expressions
    preg_match_all("/$target/i", $html, $matches);
    
    // Display the matching results
    if (!empty($matches[0])) {
        echo   "Found matches on" . " <a href='$url'>" . " this website</a>";
        foreach ($matches[0] as $match) {
            echo $match . "\n";

        }
        echo "\n";
        
    }else{
        echo "match not found";
    }
}

// Define your target value or pattern


// Define the scope (e.g., a website or web page)
$url = "https://www.$target.com";

searchWebPages($target, $url);


?>


<?php
/*

function searchWebPages($target, $urls) {
    foreach ($urls as $url) {
        $html = file_get_contents($url); // Fetch the HTML content of the web page
        $matches = [];
        
        // Extract the desired values using regular expressions
        preg_match_all("/$target/i", $html, $matches);
        
        // Display the matching results
        if (!empty($matches[0])) {
            echo "Found matches on $url:\n";
            foreach ($matches[0] as $match) {
                echo $match . "\n";
            }
            echo "\n";
        }
    }
}

// Define your target value or pattern
$target = "signup";

// Define the scope (e.g., a list of website URLs)
$urls = "https://www.google.com/";
    

searchWebPages($target, $urls);
*/
?>




AIzaSyCG-G2TdtolDqd-GXdKWSyhOl_2jq3UEAQ