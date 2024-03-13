
function validarSenha() {
    var senha1 = document.getElementById("senha");
    var senha2 = document.getElementById("confirma");
    var s1 = senha1.value;
    var s2 = senha2.value;  


    pattern = /(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,15}$/;
    if (!(pattern.test(s1))) {

        Swal.fire(
            'Favor Verificar!!!',
            'A senha informada não atende aos requisitos mínimos aceitaveis(Min 8, max 15 dígitos, letra, número e caracter especial)',
            'warning'
     )
      return false;
    }
    
    
}

function validarSenha2() {

    var senha1 = document.getElementById("senha");
    var senha2 = document.getElementById("confirma");
    var s1 = senha1.value;
    var s2 = senha2.value;  

    if (s1 != s2) {

     Swal.fire(
            'Favor Verificar!!!',
            'As senhas informadas não conferem',
            'warning'
     )
      return true;
    }

}

function validarUser() {

    var usuario = document.getElementById("usuario");

    var us = usuario.value;

}