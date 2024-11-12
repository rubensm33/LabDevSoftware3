document.addEventListener('DOMContentLoaded', () => {
    const cardContainer = document.querySelector('.card-container');

    const listarVantagens = async () => {
        try {
            const response = await axios.get('http://127.0.0.1:8000/empresas/vantagens');
            const vantagens = response.data.vantagens;

            // Inserir as vantagens nos cards
            vantagens.forEach(vantagem => {
                const card = document.createElement('div');
                card.classList.add('card');

                const link = document.createElement('a');
                link.href = `/vantagem/${vantagem.id}`;
                link.classList.add('link');

                const img = document.createElement('img');
                img.src = vantagem.foto;
                img.alt = vantagem.descricao;

                const titulo = document.createElement('h3');
                titulo.textContent = vantagem.descricao;

                const custo = document.createElement('p');
                custo.textContent = `Custo: ${vantagem.custo_moedas} 🪙`;

                const empresa = document.createElement('p');
                empresa.textContent = `Empresa: ${vantagem.empresa.nome}`;

                card.appendChild(link);
                link.appendChild(img);
                link.appendChild(titulo);
                link.appendChild(custo);
                link.appendChild(empresa);

                cardContainer.appendChild(card);
            });
        } catch (error) {
            console.error("Erro ao buscar vantagens:", error);
        }
    };

    listarVantagens();
});