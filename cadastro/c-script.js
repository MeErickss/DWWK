let btnCreate = document.querySelector('#btn_create')
let btnRegister = document.querySelector('#btn_register')
let registerMenu = document.querySelector('.register')
let welcome = document.querySelector('.welcome')

function menuRegister(){
    if (registerMenu.computedStyleMap.bottom == '-100%'  ||  registerMenu.computedStyleMap.bottom == ''){
        registerMenu.computedStyleMap.bottom = "100%"  
        
    }


}