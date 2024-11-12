async function handleSubmit(event) {
    event.preventDefault();

    const form = document.getElementById('form-cadastro');
    const formData = new FormData(form);

    const data = {
        nome: formData.get('nome'),
        cpf: formData.get('cpf'),
        rg: formData.get('rg'),
        rua: formData.get('rua'),
        bairro: formData.get('bairro'),
        numero: formData.get('numero'),
        cidade: formData.get('cidade'),
        estado: formData.get('estado'),
        email: formData.get('email'),
        senha: formData.get('senha'),
        curso: formData.get('curso'),
        instituicao: formData.get('instituicao')
    };

    try {
        const response = await fetch('http://127.0.0.1:8000/alunos/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        if (response.ok) {
            alert('Aluno cadastrado com sucesso!');
            window.location.href = '/';
        } else {
            const errorData = await response.json();
            alert(`Erro ao cadastrar aluno: ${errorData.detail}`);
        }
    } catch (error) {
        console.error('Erro:', error);
        alert('Erro ao cadastrar aluno.');
    }
}