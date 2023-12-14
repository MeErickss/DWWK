let iconMenu = document.querySelector('.mobile-menu');
let menuMobile = document.querySelector('.nav-list');

function handleMenu(){
    if (menuMobile.style.left == "-50%"  || menuMobile.style.left == ''){
        menuMobile.style.left = "50%"
        iconMenu.src = '../close.svg'
        
    } else {
        menuMobile.style.left = '-50%'
        menuMobile
        iconMenu.src = '../menu.svg';
    }
}
