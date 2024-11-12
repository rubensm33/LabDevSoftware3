document.getElementById('loginForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    const formData = new URLSearchParams();
    formData.append('username', email);
    formData.append('password', password);

    try {
        const response = await fetch('http://127.0.0.1:8000/token/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            body: formData
        });

        if (response.ok) {
            const data = await response.json();
            localStorage.setItem('token', data.access_token);
            alert('Login realizado com sucesso!');
            window.location.href = '/extrato'; // Redireciona para a página de extrato
        } else {
            const errorData = await response.json();
            alert(`Erro ao efetuar login: ${errorData.detail}`);
        }
    } catch (error) {
        console.error('Erro:', error);
        alert('Erro ao efetuar login.');
    }
});