let menuMobile = document.querySelector('.nav-list');

function handleMenu(){
    if (menuMobile.style.right == "-50%"  || menuMobile.style.right == ''){
        menuMobile.style.right = "0%"        
        menuMobile.style.transition = '0.4s'
        
    } else {
        menuMobile.style.right = '-50%'
        menuMobile.style.transition = '0.4s'
    }
}
