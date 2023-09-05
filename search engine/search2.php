<?php

// Set your Google Search API key
$apiKey = 'AIzaSyCG-G2TdtolDqd-GXdKWSyhOl_2jq3UEAQ';

// Set the search query
$query = $_POST["name"];

// Set the number of results to retrieve
$numResults = 10;

// Prepare the API request URL
$requestUrl = "https://www.googleapis.com/customsearch/v1?key=$apiKey&cx=d40dbf27c184d463d&q=" . urlencode($query) . "&num=$numResults";

// Send the API request and get the response
$response = file_get_contents($requestUrl);

// Decode the JSON response
$data = json_decode($response, true);

// Check if the response contains search results
if (isset($data['items'])) {
    // Iterate over the search results and display the title and link
    foreach ($data['items'] as $item) {
        $title = $item['title'];
        $link = $item['link'];
        
        echo "Title: $title\n" . "<br>";
        echo "Link: <a href='$link'>" . " $link </a>" . "\n\n" . "<br>";
    }
} else {
    echo "No search results found.";
}
?>



<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
<form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>">

<input type="text"  name="name">
<br><br><br>
<input type="submit" value="search">
</form>
<br><br>

<script async src="https://cse.google.com/cse.js?cx=d40dbf27c184d463d">
</script>
<div class="gcse-search">
       


</div>
</body>
</html>
