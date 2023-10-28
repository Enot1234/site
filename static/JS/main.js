// Кнопка прокрутки
var button = document.querySelector('.down_arrow')

button.onclick = function() {
    window.scrollTo({
        top: 0,
        left: 0,
        behavior: 'smooth'
    });
}

// Слайдер
var cssElement = document.querySelector('.images_slaider');
var stule = window.getComputedStyle(cssElement);
setInterval(function(){
    if(stule.transform == 'none'){
        cssElement.style.cssText = "transform: translateX(-100%)";
    } else if(stule.transform[20] == '3'){
        cssElement.style.cssText = "transform: translateX(-200%)";
    } else{
        cssElement.style.cssText = "transform: none";
    }
}, 2000)