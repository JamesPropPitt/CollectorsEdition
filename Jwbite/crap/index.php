 <?php
	include_once "connect_to_db.php";

	session_start();

	// check for logout
	if ($_GET["logout"] == "1")
	{
		session_unset();
		session_destroy();
	}

	// define variables and set to empty values
	$loginErr = $emailErr = $passwordErr = "";
	$email = $password = "";

	if ($_SERVER["REQUEST_METHOD"] == "POST") {
		if (empty($_POST["email"])) {
			$emailErr = "Email is required";
		} else {
			$email = sanatise_input($_POST["email"]);
			if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
				$emailErr = "Invalid email format";
			}
		}
		
		if (empty($_POST["password"])) {
			$passwordErr = "Password is required";
		} else {
			$password = sanatise_input($_POST["password"]);
		}
		
		if ($emailErr == "" && $passwordErr == "")
		{
			$sql = "SELECT * FROM users WHERE email='$email' and password=MD5('$password');";
			$result = $conn->query($sql);
			
			if ($result->num_rows == 1)
			{
				$row = $result->fetch_assoc();
				$_SESSION["user_id"] = $row["id"];
				$_SESSION["user_name"] = $row["name"];
				$_SESSION["user_privileges"] = $row["privileges"];
				
				// admin redirect
				if ($_SESSION["user_privileges"] == "admin")
				{
					header( "Location: admin_listusers.php" ); die;
				}
				// product owner redirect
				else if ($_SESSION["user_privileges"] == "product owner")
				{
					header( "Location: po_teams.php" ); die;
				}
				// student redirect
				else
				{
					header( "Location: student_peerreview.php" ); die;
				}
				
			} else {
				$loginErr = "Incorrect email or password. Please try again";
			}
		}
	}


?>
<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" type="text/css" href="stylesheet.css">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
<div class="row">
<div class="col-2"></div>
<div class="col-10">
<h2>Games Academy P.O. Meeting Tracker</h2>
Please log in below.
<?php
	if ($loginErr != "")
	{
		echo "<br><br>\n<span class=\"error\">" . $loginErr . "</span><br>";
	}
?>
</div>
</div>
<form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">
<div class="row">
<div class="col-2"></div>
<div class="col-1">Email:</div>
<div class="col-2">
<input style="width:100%" type="text" name="email" value="<?php echo $email;?>"/>
<span class="error"> <?php echo $emailErr;?></span>
</div>
<div class="col-7"></div>
</div>
<div class="row">
<div class="col-2"></div>
<div class="col-1">Password:</div>
<div class="col-2">
<input style="width:100%" type="password" name="password" value="<?php echo $password;?>"/>
<span class="error"> <?php echo $passwordErr;?></span>
</div>
<div class="col-7"></div>
</div>
<div class="row">
<div class="col-2"></div>
<div class="col-1">
<input type="submit" name="submit" value="Submit">
</div>
<div class="col-9"></div>
</div>
</form>
</body>
</html>