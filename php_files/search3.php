<?php
    if (isset($_GET['keyword'])){
        $searchKeyword = $_GET['keyword'];
    }
    else{
        $searchKeyword = "";
    }
    
    if (isset($_GET['pageno'])){
        $pageno = $_GET['pageno'];
    }
    else{
        $pageno = 1;
    }
	
    if (isset($_GET['allresultcount'])){
        $allresultcount = $_GET['allresultcount'];
    }
    else{
        $allresultcount = 0;
    }
	
    if (isset($_GET['refb'])){
        $fdback = $_GET['refb'];
    }
	else{
		$fdback = [];
	}
	
?>
<html>
<head>

<meta http-equiv="content-type" content="text/html; charset=UTF-8">
<style>

#header {
background-color:#4CAF50;
color:white;
text-align:center;
padding:5px;
}

#nav {
    line-height:30px;
    background-color:#eeeeee;
    width:15%;
    float:left;
}
#right {
    float:right;
    width:85%;
}

legend{font-weight:bold; font-size:24px;}

#menu ul {
height: auto;
padding: 8px 0px;
margin: 0px;
text-align:center;
}
#menu li {
display: inline;
padding: 20px;
text-align:center;
}
#menu a {
text-decoration: none;
color: black;
padding: 8px 8px 8px 8px;
}
#menu a:hover {
color: #F90;
background-color: #FFF;
}
#navmenu ul {
height: auto;
padding:0px;
margin: 0px;
text-align:center;
list-style-type: none;
}
#navmenu li {
padding: 0px;
text-align:center;
}
#navmenu a {
text-decoration: none;
color: black;
padding: 8px 8px 8px 8px;
}
#menu a:hover {
color: #F90;
background-color: #FFF;
}
.button {
    background-color: #4CAF50;
    border: none;
    color: white;
    padding: 15px 32px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    margin: 4px 2px;
    cursor: pointer;
}

html *
{
    font-family: Century Gothic, sans-serif;
}

.label{
    padding: 15px 32px;
    text-align: center;
    font-size: 16px;
    margin: 4px 2px;
}

.textline{
    padding: 12px 15px;
    font-size: 16px;
    margin: 4px 2px;
    width:500px;
}

.left{margin-left:150px;}

.input{width:350px;}

table#t01 {
    border-collapse: collapse;
	width:90%;
	cellspacing:10px;
}
table#t01 tr {
    background-color: #fff;
    border: solid;
    border-width: 1px 0;
}

table#t01 td:nth-child(even){
	width:20%;
}
table#t01 td:nth-child(odd){
	width:80%;
}

#switcher {
    text-align: right;
    background: #FFF;
}

.button2 {

    border: none;
    color: #4CAF50;
    padding: 5px 5px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    margin: 4px 2px;
    cursor: pointer;
}



</style>

<title>KU Information Retrieval System</title>

</head>

<body>

<div id="header">
<h1>KU Information Retrieval System</h1>
</div>

<div id="nav">
<ul>
<li><a href="mainpage.php">Search Engine 1</a></li>
<li><a href="search2.php">Search Engine 2</a></li>
<li><a>Search Engine 3</a></li>
</ul>
</div>

<div id="right">

<fieldset>
<legend>Search Engine 3: Relevance Feedback</legend>

<form name="searchForm" method="get" action="<?php echo $_SERVER['PHP_SELF']; ?>" onSubmit="return InputCheck(this)">
<p>
<label for="keyword" class="label">Input your Query: </label>
<input id="keyword" name="keyword" class="textline" value = "<?php echo $searchKeyword?>" type="text" class="input" />
<input id="pageno" name = "pageno" value = "<?php echo $pageno?>" type="hidden"/>
<input type="submit" class="button" name="submit" value="Search"/>
<p/>


</form>



<?php if ($searchKeyword != ""): ?>
	
	
<!--		<form name="fbForm" method="get" action="<?php echo $_SERVER['PHP_SELF']; ?>">
			<p>
			<input id="keyword" name="keyword" value = "<?php echo $searchKeyword?>" type="hidden" />
			<input id="pageno" name = "pageno" value = "<?php echo $pageno?>" type="hidden"/>
			<input id="fdback" name = "fdback" value = "<?php echo $_GET['refb_1']?>" type="hidden"/>
			<input type = "submit" class="button" value="FeedBack">
			</p>
		</form>-->

<?php
    require_once("php_python.php");
    //$indice = ppython("togetherIndiceResult::together_indice_result2", $searchKeyword,$pageno);
	$indice = [];
	if (empty($fdback)){
		$indice = ppython("togetherIndiceResult::together_indice_result2", $searchKeyword,$pageno);
	}
	else{
		$indice = ppython("togetherIndiceResult::together_indice_result3",$searchKeyword,$pageno,$fdback);
	}
    
?>

<form name="fbForm" method="get" action="<?php echo $_SERVER['PHP_SELF']; ?>">
	<input id="keyword" name="keyword" value = "<?php echo $searchKeyword?>" type="hidden" />
	<input id="pageno" name = "pageno" value = "<?php echo $pageno?>" type="hidden"/>
	<input type = "submit" class="button" value="FeedBack">
<hr>
    <table id = "t01" border=1 frame=void rules=rows>

        <?php
			$iter_num=1;
            foreach($indice as $value){
                echo '<tr><td>';
                //echo $value;
                //echo "file://$value";
				$allresultcount = $value[3];
                echo "<a href=\"$value[0]\" target=\"_blank\">$value[0]</a>";
                echo '</td>';
				//echo '<td>Relavent<br>';
				//echo 'Non-relavent</td>';
				echo '<td>';
				echo "<p><select name = \"refb[]";
				echo $iter_num;
				echo "\">
					<option value=\"0\">None</option>
					<option value=\"1\">Relevant</option>
					<option value=\"2\">Non-Relevant</option>
					</p>";	
				$iter_num++;
				echo '</td>';
				echo '<tr><td>';
				$space_separated = "...";
				foreach($value[2] as $itemkey=>$itemvalue){
					if(in_array($itemkey, $value[1])){
						$space_separated = $space_separated."<mark>".$itemvalue."</mark> ";
					}
					else{
						$space_separated = $space_separated.$itemvalue." ";
					}
				}
				echo $space_separated."...";
				echo '</td></tr>';
            }
        ?>
    </table>
</hr>
</form>


<div id="switcher">
        <div class="button2" id="switcher-first">
		<a href="mainpage.php?keyword=<?php echo $searchKeyword?>&pageno=<?php echo '1'?>">FIRST</a>
        </div>
        <div class="button2" id="switcher-prev">
			
			<?php if (intval($pageno) > 1): ?>
				<?php 					
					$new_pageno = intval($pageno)-1;
				?>
				<a href="mainpage.php?keyword=<?php echo $searchKeyword?>&pageno=<?php echo $new_pageno?>">PREV</a>
			<?php else: ?>
				PREV
        	<?php endif; ?>
        </div>
        <div class="button2" id="switcher-next">
			<?php
			$pagecount = round($allresultcount/20);
			?>
			<?php if ( $pageno < $pagecount): ?>
			<?php 
				
				$new_pageno = intval($pageno)+1;
				//echo $new_pageno;
			?>
			<a href="mainpage.php?keyword=<?php echo $searchKeyword?>&pageno=<?php echo $new_pageno?>">NEXT</a>
			<?php else: ?>
        		NEXT
			<?php endif; ?>
        </div>
        <div class="button2" id="switcher-last">
			<?php
			$pagecount = round($allresultcount/20);
			?>
			<a href="mainpage.php?keyword=<?php echo $searchKeyword?>&pageno=<?php echo $pagecount?>">LAST</a>      
        </div>
</div>


<?php endif; ?>
</fieldset>

</div>

<script language=JavaScript>
<!--
function InputCheck(LoginForm)
{
   if (searchForm.keyword.value == "")
  {
    alert("Input cannot be empty!");
    searchForm.keyword.focus();
    return (false);
  }
}
//-->
</script>


<!-- <?php echo '<p>Hello World</p>'; ?> -->
</body>
</html>