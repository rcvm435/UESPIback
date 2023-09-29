// Abrir/fechar o menu lateral
const openMenuButton = document.getElementById('open-menu');
const sideMenu = document.getElementById('side-menu');

openMenuButton.addEventListener('click', () => {
    sideMenu.classList.toggle('opened');
});

// Exemplo de adicionar opções ao menu
// Isso pode ser feito dinamicamente com JavaScript em uma aplicação real
const menuContent = document.createElement('ul');
menuContent.innerHTML = `
    <li><a href="#">Categorias</a></li>
    <li><a href="#">Ofertas</a></li>
    <li><a href="#">Ajuda</a></li>
    <li><a href="#">Contato</a></li>
`;

sideMenu.appendChild(menuContent);
