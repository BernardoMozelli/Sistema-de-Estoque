<?php

  //criei variaveis para receber as credenciais de acesso ao meu banco de dados instalado no xampp
  $servidor = "localhost";
  $user = "bernardo";
  $pass = "250317";
  $dbname = "inventario_pmsl";

  //criar a conexão com o banco de dados.
  $conex = new mysqli($servidor, $user, $pass, $dbname); 

  if ($conex->connect_error) {
    die("Connection failed: " . $conex->connect_error);
  }

  $usuario = filter_input(INPUT_POST, 'usuario', FILTER_SANITIZE_STRING);

  $senha = filter_input(INPUT_POST, 'confirma', FILTER_SANITIZE_EMAIL);  

  $result_cadastro = "UPDATE cadastro SET senha='$senha' WHERE usuario = '$usuario'";

  if ($conex->query($result_cadastro) === TRUE) {
  

  } else {
  echo "Error updating record: " . $conex->error;
  }

  $conex->close();

?>