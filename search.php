<?php
header("Access-Control-Allow-Origin: *");
$in = $_GET['term'];
$out = shell_exec("./search.py \"$in\"");
echo "$out";
?>
