<?php
$url = 'https://api.revlo.co/1/redemptions?page=1&refunded=false';
$opts = array(
		'http'=>array(
				'method'=>"GET",
				'header'=>"Accept-language: en\r\n" .
				"Cookie: foo=bar\r\n" .
				"x-api-key: YcFVQiXIwW0RBlNfYMuahA-uaCxQPyjUIWL4xHD0MI8\r\n"
		)
);

$context = stream_context_create($opts);

// Open the file using the HTTP headers set above
$file =  json_decode(file_get_contents($url, false, $context));
header('Content-Type: application/json');
print json_encode($file, JSON_PRETTY_PRINT);