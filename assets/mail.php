<?php

$recepient = "sania_piter@mail.ru";
$sitename = "FortyTwoTestTask";

$name = trim($_GET["name"]);
$phone = trim($_GET["phone"]);
$text = trim($_GET["text"]);

$pagetitle = "Нова заявка з сайту \"$FortyTwoTestTask\"";
$message = "Имя: $name \nТелефон: $phone \nТекст: $text";
mail($recepient, $pagetitle, $message, "Content-type: text/plain; charset=\"utf-8\"\n
?>