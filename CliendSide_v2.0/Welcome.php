<?php

session_start();

if(isset($_SESSION['email']))
{
    echo '<div style="background-color: #f5f5f5; padding: 10px; text-align: center;">';
    echo 'Welcome '.$_SESSION['email'].'<br>';
    echo '<a href="Backtohome.php?Backtohome" style="color: #333; text-decoration: none;">Home</a>';
    echo '</div>';
}
else
{
    header("location:homepage.html");
}

?>
