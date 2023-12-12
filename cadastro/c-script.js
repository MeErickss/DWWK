let btnCreate = document.querySelector('#btn_create')
let btnRegister = document.querySelector('#btn_register')
let registerMenu = document.querySelector('.register')
let welcome = document.querySelector('.welcome')

function menuRegister(){
    if (registerMenu.computedStyleMap.bottom == '-100%'  ||  registerMenu.computedStyleMap.bottom == ''){
        registerMenu.computedStyleMap.bottom = "100%"     
    }
}

function register() {
    let name = document.getElementById('input_name').value;
    let email = document.getElementById('input_email').value;
    let senha = document.getElementById('input_password').value;

    if (name == '') {
        alert('Insira um nome para efetuar o cadastro!');

    } else if (email == '') {
        alert('Insira um email para efetuar o cadastro!');

    } else if (senha.length < 8) {
        alert('A senha deve conter 8 ou mais caracteres!');
        
    } else {
        alert('Cadastro Realizado!');
        
        document.getElementById('input_name').value = '';
        document.getElementById('input_email').value = '';
        document.getElementById('input_password').value = '';
    }
}