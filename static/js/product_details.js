// CÓDIGO JAVASCRIPT PARA A PÁGINA DE DETALHES DO PRODUTO

var MainImg = document.getElementById("MainImg");
var SmallImg = document.getElementsByClassName("small-img");

SmallImg[0].onclick = function () {
  MainImg.src = SmallImg[0].src;
}

SmallImg[1].onclick = function () {
    MainImg.src = SmallImg[1].src;
}

SmallImg[2].onclick = function () {
  MainImg.src = SmallImg[2].src;
}

SmallImg[3].onclick = function () {
    MainImg.src = SmallImg[3].src;
}