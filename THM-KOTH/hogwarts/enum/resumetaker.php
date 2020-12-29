<?php
if($_FILES['uploadedfile']['type'] != "application/pdf") {
echo "Sorry, we only allow uploading your resumes in magical PDF formats. ";

exit;
}
$uploaddir = 'uploads/';
$uploadfile = $uploaddir.basename($_FILES['uploadedfile']['name']);
if (copy($_FILES['uploadedfile']['tmp_name'], $uploadfile)) {
echo "File is valid, and was successfully uploaded.\n";
} else {
echo "File uploading failed.\n";
}
?>

