<?php

session_start();

if(isset($_SESSION['username']))
{
    echo 'Hi   '.'<br/>>';
    echo 'ThankYou for Registeriing With us'   .'<br/>>';
    echo '<a href="Backtohome.php?Backtohome"> Home  </a>';
}
else
{
    echo '<div style="background-color: #de97ce; padding:400px; font-size:36px; text-align: center;">';
    echo 'Hi   '.'<br/>>';
    echo 'ThankYou for Registeriing With us'   .'<br/>>';
    echo '<a href="Backtohome.php?Backtohome"> Home  </a>';
}
?>
