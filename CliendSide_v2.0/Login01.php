<?php

session_start();
require_once('logconnect.php');

if(isset($_POST['Login'])) 
{

} else
    {
    if(empty($_POST['email']) || empty($_POST['password']))
    {
        header("location:login.html?empty=Fields cannot be Empty");
    }
    else
    {
        $query="select * from registration where email='".$_POST['email']."' and password='".$_POST['password']."'";
        $result=mysqli_query($conn, $query);

        if(mysqli_fetch_assoc($result))
        {
            $_SESSION['email']=$_POST['email'];
            header("location:Welcome.php");
        }
        else
        {
            header("location:login.html?Invalied=please enter valied email and password");
        }

    }
}

    





?>

