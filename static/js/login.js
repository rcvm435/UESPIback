//  BUTTON-JURIDICA
 
 // Função para redirecionar o usuário para outro tipo de login
  function redirectLogJur() {
    // Altere a URL abaixo para a página de login desejada
    window.location.href = "/juridica/login/";
  }

  // Adicionar um ouvinte de evento de clique ao botão
  document.getElementById("login-juridica").addEventListener("click", redirectLogJur);



//   BUTTON FISICA
function redirectLogFis() {
    window.location.href = "/fisica/login/";
  }

  // Adicionar um ouvinte de evento de clique ao botão
  document.getElementById("login-fisica").addEventListener("click", redirectLogFis);