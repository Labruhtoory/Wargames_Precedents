<?php
        $servername = "localhost";
        $username = "root";
        $password = "neville_was_chosen";
        $db = "students";
        $FLAG = "THM{wait-for-your-letter!}";

        $conn = new mysqli($servername, $username, $password, $db);

        // Check connection
        if ($conn->connect_error) {
                die("Connection failed");
        }
?>

