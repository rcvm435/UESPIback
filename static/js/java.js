// PÁGINA JAVASCRIPT PARA A HOME

const header = document.querySelector("header");

window.addEventListener ("scroll", function(){
    header.classList.toggle("sticky", this.window.scrollY > 0);
})

let menu = document.querySelector('#menu-icon');
let navmenu = document.querySelector('.navmenu');

menu.onclick = () => {
    menu.classList.toggle('bx-x');
    navmenu.classList.toggle('open');
}


document.getElementById("scroll-to-bottom").addEventListener("click", function(e) {
    e.preventDefault(); // Impede que o link funcione normalmente

    // Role a página para o final
    window.scrollTo(0, document.body.scrollHeight);
});




