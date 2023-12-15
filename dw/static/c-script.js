let registerMenu = document.querySelector('.register')
let backG = document.querySelector('#back-image')

function menuRegister() {
    if (registerMenu.style.bottom == '-100%'  ||  registerMenu.computedStyleMap.bottom == ''){
        registerMenu.style.bottom = '0'
        registerMenu.style.transition = '0.4s' 
        backG.style.opacity = '0.5'
        backG.style.transition = '0.4s'

    
    } else {
        registerMenu.style.bottom = '-100%'

    }
}

function register() {
    let name = document.getElementById('id_user').value;
    let email = document.getElementById('id_email').value;
    let senha = document.getElementById('id_pass').value;

    if (name == '') {
        alert('Insira um nome para efetuar o cadastro!');

    } else if (email == '') {
        alert('Insira um email para efetuar o cadastro!');

    } else if (senha.length < 8) {
        alert('A senha deve conter 8 ou mais caracteres!');
        
    } else {
        alert('Cadastro Realizado!');
        
        document.getElementById('id_user').value = '';
        document.getElementById('id_email').value = '';
        document.getElementById('id_pass').value = '';
    }
}