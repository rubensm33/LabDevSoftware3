async function fetchExtrato() {
        try {
            const saldoResponse = await fetch('http://127.0.0.1:8000/alunos/saldo', {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer ' + localStorage.getItem('token') // Assumindo que o token está armazenado no localStorage
                }
            });

            const transacoesResponse = await fetch('http://127.0.0.1:8000/alunos/transacoes', {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer ' + localStorage.getItem('token') // Assumindo que o token está armazenado no localStorage
                }
            });

            if (saldoResponse.ok && transacoesResponse.ok) {
                const saldoData = await saldoResponse.json();
                const transacoesData = await transacoesResponse.json();

                document.getElementById('saldo-atual').innerText = saldoData.saldo_moedas;

                const transacoesContainer = document.getElementById('transacoes-container');
                transacoesContainer.innerHTML = '';

                transacoesData.forEach(transacao => {
                    const transacaoElement = document.createElement('div');
                    transacaoElement.classList.add('box');
                    transacaoElement.innerHTML = `
                        <p>${transacao.tipo === 'recebimento' ? 'Recebeu de' : 'Resgatou o item:'} ${transacao.participante} = ${transacao.quantidade} | Descrição: ${transacao.motivo}</p>
                        <div class="divider"></div>
                    `;
                    transacoesContainer.appendChild(transacaoElement);
                });
            } else {
                alert('Erro ao buscar extrato do aluno.');
            }
        } catch (error) {
            console.error('Erro:', error);
            alert('Erro ao buscar extrato do aluno.');
        }
    }

    document.addEventListener('DOMContentLoaded', fetchExtrato);
document.addEventListener('DOMContentLoaded', fetchExtrato);