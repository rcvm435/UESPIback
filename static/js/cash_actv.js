// COLOCAR TRANSAÇÕES NA TABELA DE ATIVIDADES DE CASHBACK -- DASHBOARD DE PESSOA FÍSICA

Activities.forEach(activity=> {
    const tr = document.createElement('tr');
    const trContent = `
                       <td>${activity.storeName}</td>
                       <td>${activity.cashValue}</td>
                       <td>${activity.orderDate}</td>
                       <td class="${activity.verify === 'Cancelado' ? 'danger' : activity.verify === 'Pendente' ? 'warning' : 'primary'}">${activity.verify}</td>
                       <td class="primary">Detalhes</td>
                      `;
    tr.innerHTML = trContent;
    document.querySelector('table tbody').appendChild(tr);
})