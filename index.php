
<html>
<head>
<title><?php echo "cool title";?></title></head>
<style>
	body{
		background-color: #55acee;
	}
</style>
<body
<?php 
//$image_url='https://www.google.com/intl/en_com/images/srpr/logo3w.png';
//echo $image_url;
?>
<p>
<div style="float : left; size:50%;">
<img src="img\twiiterfont.png"  width="210" height="210" border="0">
</div>
<br>
<?php echo '<link rel="style.css" type="text/css" href="style.css"></head>'; ?>  
<form method = "post">
Search: <input type="text" name="searchbox">
<input type="submit" value="Submit">
<br>
<input type="radio" name="algorithm" id="kmp" value="kmp"> KMP
<br>
<input type="radio" name="algorithm" id="booyer" value="booyer"> Booyer
<br>
<input type="radio" name="algorithm" id="regex" value="regex"> Regex
</form>
<?php
	if(isset($_POST['searchbox'])){
		$item = $_POST['searchbox'];
		if(isset($_POST['algorithm'])){
			if($_POST['algorithm'] == 'kmp'){
				$tmp = shell_exec("python knuth_morris_pratt.py $item");
			} else if ($_POST['algorithm'] == 'booyer'){
				$tmp = shell_exec("python boyer_moore.py $item");
			} else if ($_POST['algorithm'] == 'regex'){
				$tmp = shell_exec("python regex.py $item");
			}
    		    
    	$s = explode("---------------------------------------------------------------", $tmp);
    	foreach ($s as $m) {
    		echo $m;
    		echo "<br>";
    	}
    }
    else{
    	echo "Select the algorithm first\n";
    }
   }
?>
</p>

</body>
</html>