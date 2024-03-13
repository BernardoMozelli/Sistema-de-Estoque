
<!DOCTYPE html>
<html lang="pt-br">
<head>

	<title>Esqueci minha Senha</title>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
<!--===============================================================================================-->	
	<link rel="icon" type="image/png" href="images/icons/logo_icone.ico"/>
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="vendor/bootstrap/css/bootstrap.min.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="fonts/font-awesome-4.7.0/css/font-awesome.min.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="fonts/iconic/css/material-design-iconic-font.min.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="vendor/animate/animate.css">
<!--===============================================================================================-->	
	<link rel="stylesheet" type="text/css" href="vendor/css-hamburgers/hamburgers.min.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="vendor/animsition/css/animsition.min.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="vendor/select2/select2.min.css">
<!--===============================================================================================-->	
	<link rel="stylesheet" type="text/css" href="vendor/daterangepicker/daterangepicker.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="css/util.css">
	<link rel="stylesheet" type="text/css" href="css/main.css">
<!--===============================================================================================-->
    <link rel="folha de estilo" href="https://cdn.jsdelivr.net/npm/sweetalert2@11.7.31/dist/sweetalert2.
									 min.css">

</head>
<body>
 <form method="POST" action="conexao.php">
	 <script src="js/passw.js"></script>
	 <div class="limiter">			
		<div class="container-login100">	
			<div class="wrap-login100">
				<img class="img_logo" src="images/logos/logo_transparent.png"/>	
				<form class="login100-form validate-form">
					<span class="login100-form-title p-b-26">
						REDEFINIR SENHA
                  		<br />
                  		<br />
					</span>

					<div class="wrap-input100 validate-input">
						
						<input class="input100" type="text" name="usuario" id="usuario">
						
						<span class="focus-input100" data-placeholder="Insira o seu nome de usuário"> <br /> <br /></span>
			        </div>

               		<div class="wrap-input100 validate-input" >
						<span class="btn-show-pass">
							<i class="zmdi zmdi-eye"></i>
						</span>
						
						<input class="input100" type="password" name="senha" id="senha" onblur="return validarSenha()">
						
						<span class="focus-input100" data-placeholder="Insira uma nova senha"> <br /> <br /></span>

			        </div>

					<div class="wrap-input100 validate-input">
						<span class="btn-show-pass">
							<i class="zmdi zmdi-eye"></i>
						</span>
						<input class="input100" type="password" name="confirma" id="confirma" onblur="return validarSenha(), validarSenha2()">

						<span class="focus-input100" data-placeholder="Confirme a senha"></span>

					</div>

					<div class="container-login100-form-btn">
						<div class="wrap-login100-form-btn">
							<div class="login100-form-bgbtn"></div>
							<button type="submit" class="login100-form-btn" onblur="return validarSenha(), validarSenha2()">
								ALTERAR
							</button>
						</div>
					</div>
						</a>
					</div>
				</form>
			</div>
		</div>
	 </div>

	 <div id="dropDownSelect1"></div>

	 <!--===============================================================================================-->
	  <script src="https://cdn.jsdelivr.net/npm/sweetalert2@11.7.31/dist/sweetalert2.all.min.js"></script>
 	 <!--===============================================================================================-->
      <script src="vendor/jquery/jquery-3.2.1.min.js"></script>
 	 <!--===============================================================================================-->
	  <script src="vendor/animsition/js/animsition.min.js"></script>
 	 <!--===============================================================================================-->
	  <script src="vendor/bootstrap/js/popper.js"></script>
	  <script src="vendor/bootstrap/js/bootstrap.min.js"></script>
 	 <!--===============================================================================================-->
	  <script src="vendor/select2/select2.min.js"></script>
 	 <!--===============================================================================================-->
	  <script src="vendor/daterangepicker/moment.min.js"></script>
	  <script src="vendor/daterangepicker/daterangepicker.js"></script>
 	 <!--===============================================================================================-->
	  <script src="vendor/countdowntime/countdowntime.js"></script>
 	 <!--===============================================================================================-->
      <script src="js/main.js"></script>

   </form>

</body> 
</html>