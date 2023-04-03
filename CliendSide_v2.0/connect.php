<?php
    $username=$_POST['username'];
    $email=$_POST['email'];
    $password=$_POST['password'];
    
    $conn=new mysqli('localhost','root','','testt');
    if($conn->connect_error){
        die('Connection Failed : '.$conn->connect_error);
    }else{
        $stmt=$conn->prepare("Insert into registration(username,email,password)
        values(?,?,?)");
        $stmt->bind_param("sss",$username,$email,$password);
        $stmt->execute();
        echo 'alert ("Registration Successful")';
        $stmt->close();
        $conn->close();
    }
    $_SESSION['username']=$_POST['username'];
            header("location:Welcome02.php");
?>