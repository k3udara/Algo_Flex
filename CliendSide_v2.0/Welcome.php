<?php

session_start();

if(isset($_SESSION['email']))
{
    echo '<div style="background-color: #de97ce; padding:400px; font-size:46px; text-align: center;">';
    echo 'Welcome '.$_SESSION['email'].'<br>';
    echo '<a href="Backtohome.php?Backtohome" style="color: #333; text-decoration: none;">Home</a>';
    echo '</div>';
}
else
{
    header("location:homepage.html");
}

?>
