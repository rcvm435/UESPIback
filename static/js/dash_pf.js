// ARQUIVO JAVASCRIPT PARA A PÁGINA DASHBOARD DO USUÁRIO PESSOA FÍSICA

const sideMenu = document.querySelector("aside");
const menuBtn = document.querySelector("#menu-btn");
const closeBtn = document.querySelector("#close-btn");
const themeToggler = document.querySelector(".theme-toggler");

// ABRIR SIDEBAR
menuBtn.addEventListener("click", () => {
    sideMenu.style.display = 'block';
})

//FECHAR SIDEBAR
closeBtn.addEventListener("click", () => {
    sideMenu.style.display = 'none';
})

// ESCOLHER TEMA
themeToggler.addEventListener('click', () => {
    document.body.classList.toggle('dark-theme-variables');

    themeToggler.querySelector('span:nth-child(1)').
    classList.toggle('active');
    themeToggler.querySelector('span:nth-child(2)').
    classList.toggle('active');

})

// COLOCAR PEDIDOS NA TABELA
Orders.forEach(order => {
    const tr = document.createElement('tr');
    const trContent = `
                       <td>${order.productName}</td>
                       <td>${order.productNumber}</td>
                       <td>${order.orderDate}</td>
                       <td class="${order.shipping === 'Cancelado' ? 'danger' : order.shipping === 'Pendente' ? 'warning' : 'primary'}">${order.shipping}</td>
                       <td class="primary">Detalhes</td>
                      `;
    tr.innerHTML = trContent;
    document.querySelector('table tbody').appendChild(tr);
})

// REDIRECIONAR PARA A PÁGINA DE CASHBACK ATRAVÉS DOS INSIGHTS
const cashback = document.getElementById("cashback");

cashback.addEventListener("click", function() {
    const pageURL = cashback.getAttribute("data-url");

    if (pageURL) {
        window.location.href = pageURL;
    }
});


