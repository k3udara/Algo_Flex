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
    echo 'Hi   '.'<br/>>';
    echo 'ThankYou for Registeriing With us'   .'<br/>>';
    echo '<a href="Backtohome.php?Backtohome"> Home  </a>';
}
?>