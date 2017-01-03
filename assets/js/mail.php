<?php

$recepient = "sania_piter@mail.ru";
$sitename = "FortyTwoTestTask";

$name = trim($_POST["name"]);
$phone = trim($_POST["phone"]);
$text = trim($_POST["text"]);

$pagetitle = "Нова заявка з сайту \"$FortyTwoTestTask\"";
$message = "Имя: $name \nТелефон: $phone \nТекст: $text";
mail($recepient, $pagetitle, $message, "Content-type: text/plain; charset=\"utf-8\"\n
?>