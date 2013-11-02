<?php

$url = 'http://hermes.wha.la/api/hermes';
$data = array('Command'=>'INIT',
        'Token' =>  '3b00ea6d-1383-4fdc-a6a8-9578091947f9',
        'ChangeRequest'=> None);

// use key 'http' even if you send the request to https://...
$data_string = json_encode($data);

$ch = curl_init('http://api.local/rest/users');                                                                      
curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "POST");                                                                     
curl_setopt($ch, CURLOPT_POSTFIELDS, $data_string);                                                                  
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);                                                                      
curl_setopt($ch, CURLOPT_HTTPHEADER, array(                                                                          
    'Content-Type: application/json',                                                                                
    'Content-Length: ' . strlen($data_string))                                                                       
);                                                                                                                   
 
$result = curl_exec($ch);
/*
$options = array(
    'http' => array(
        'header'  => "Content-type: application/x-www-form-urlencoded\r\n",
        'method'  => 'POST',
        'content' => http_build_query($data),
    ),
);
$context  = stream_context_create($options);
$result = file_get_contents($url, false, $context);
*/
var_dump($result);

?>