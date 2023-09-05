c<?php
// define variables and set to empty values
$nameErr = $emailErr = $passwordErr = "";
$name = $email = $password = "";

if ($_SERVER["REQUEST_METHOD"] == "POST") {
  if (empty($_POST["name"])) {
    $nameErr = "Name is required";
  } else {
    $name = test_input($_POST["name"]);
    // check if name only contains letters and whitespace
    if (!preg_match("/^[a-zA-Z-' ]*$/", $name)) {
      $nameErr = "Only letters and white space allowed";
    }
  }

  if (empty($_POST["password"])) {
    $passwordErr = "Password is required";
  } else {
    $password = test_input($_POST["password"]);
  }

  if (empty($_POST["email"])) {
    $emailErr = "Email is required";
  } else {
    $email = test_input($_POST["email"]);
    // check if e-mail address is well-formed
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
      $emailErr = "Invalid email format";
    }
  }
}

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
  <title>signup page</title>
  <link rel="stylesheet" href="login.css">
</head>

<body style="background-image: url('http://localhost/website/image.avif') ; background-size: cover; ">

  <div class="space">
  </div>
  <center>
    <div class="container">
      <form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>">
        <h1>signup</h1>
        <div class="input-box">
          <input type="text" name="name" placeholder="username" value="<?php echo $name; ?>">
          <span class="error"> <?php echo $nameErr; ?></span>

        </div>
        <div class="input-box">
          <label for="email" style="color: darkgray; float: left;"> email</label> <br>
          <input type="email" placeholder=" text@gmail.com" name="email" value="<?php echo $email; ?>">
          <span class="error"><?php echo $emailErr; ?></span>
        </div>
        <div class="input-box">
          <br>

          <label for="password" style="color: darkgray; float: left;"> password</label>
          <input type="password" placeholder=" enter password" name="password" class="over_flow" value="<?php echo $password; ?>" class="over_flow">
          <span class="error"> <?php echo $passwordErr; ?></span>

        </div>
        <!-- <div class="input-box message-box">
                
              </div> --><br><br>
        <div class="button">
          <input type="submit" value="Create Account" value="Submit">
        </div><br><br>
        <label for="login">Already have an account? <span><a href="login.php" style="color: blueviolet; text-decoration-line: none;"> Login</a></span></label>
      </form>
    </div>
  </center>
</body>

</html>
<?php


$password = password_hash($_POST["password"], PASSWORD_DEFAULT);
if (empty($_POST["email"])) {
  echo '';
} else {
  $mysqli = require __DIR__ . "/conn.php";
  $stmt = $conn->prepare("INSERT INTO `users`( `name`, `email`, `password`)  VALUES (?, ?, ?)");
  $stmt->bind_param("sss", $name,  $email, $password);

  if ($stmt->execute()) {
    header("Location: indexs.php");
    exit;
  }
  echo "<h1>" . "data exist" . "</h1>";

  $stmt->close();
  $conn->close();
}
?>