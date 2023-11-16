// PÁGINA JAVASCRIPT PARA O CARRINHO

// Abrir e fechar o carrinho
let cartIcon = document.querySelector('#cart-icon');
let cart = document.querySelector('.cart');
let closeCart = document.querySelector('#close-cart');

console.log(cartIcon, cart, closeCart);

cartIcon.onclick = () => {
    cart.classList.add('active');
};

closeCart.onclick = () => {
    cart.classList.remove('active');
};

// Adicionar itens ao carrinho
if (document.readyState == 'loading') {
    document.addEventListener('DOMContentLoaded', ready);
} else {
    ready();
}

// Remover itens do carrinho
function ready() {
    var removeCartButtons = document.getElementsByClassName('cart-remove'); 
    console.log(removeCartButtons);
    for (var i = 0; i < removeCartButtons.length; i++) {
        var button = removeCartButtons[i];
        button.addEventListener('click', removeCartItem);
    }
    // Escolher quantidade de itens
    var quantityInputs = document.getElementsByClassName('cart-quantity');
    for (var i = 0; i < quantityInputs.length; i++) {
        var input = quantityInputs[i];
        input.addEventListener('change', quantityChanged);
    }
    // Adicionar ao carrinho
    var addToCartButtons = document.getElementsByClassName('add-to-cart');
}

function removeCartItem(event) {
    var buttonClicked = event.target;
    buttonClicked.parentElement.remove();
    updateTotal();
}

function quantityChanged(event) {
    var input = event.target;
    if (isNaN(input.value) || input.value <= 0) {
        input.value = 1;
    }
    updateTotal();
}

// Atualizar valor total do carrinho
function updateTotal() {
    var cartContent = document.getElementsByClassName('cart-content')[0];
    var cartBoxes = cartContent.getElementsByClassName('cart-box');

    var total = 0;
    for (var i = 0; i < cartBoxes.length; i++) {
        var cartBox = cartBoxes[i];

        var priceElement = cartBox.getElementsByClassName('cart-price')[0];
        var quantityElement = cartBox.getElementsByClassName('cart-quantity')[0];

        var price = parseFloat(priceElement.innerText.replace('R$', ''));
        var quantity = quantityElement.value;

        total = total + (price * quantity);

        total = Math.round(total * 100) / 100;
        document.getElementsByClassName('total-price')[0].innerText = 'R$' + total;
    }

}