<?php

include "settings.php";

try {

  $redis = new Redis();
  $redis->connect($databases['redis']['host'], $databases['redis']['port']);
  $redis->set("message", "Hello World");
	print($redis->get("message") . PHP_EOL) ;

}
catch (Exception $e) {
	die($e->getMessage());
}
