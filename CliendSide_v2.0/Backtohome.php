<?php

session_start();
if(isset($_GET['Home']))
{
    session_destroy();
    header("location:homepage.html");
}
else
{
    header("location:homepage.html");
}

?>