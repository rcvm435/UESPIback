// SCRIPT PARA ADICONAR OS DADOS NA TABELA PEDIDOS / PÁGINA DE PEDIDOS / DASHBOARD PESSOA JURÍDICA

Activities.forEach(activity=> {
    const tr = document.createElement('tr');
    const trContent = `
                       <td>${activity.number}</td>
                       <td>${activity.productNumber}</td>
                       <td>${activity.paymentStatus}</td>
                       <td class="${activity.shipping === 'Cancelado' ? 'danger' : activity.shipping === 'Pendente' ? 'warning' : 'primary'}">${activity.shipping}</td>
                       <td class="primary">Detalhes</td>
                      `;
    tr.innerHTML = trContent;
    document.querySelector('table tbody').appendChild(tr);
})