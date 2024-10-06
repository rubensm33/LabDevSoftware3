# Histórias de Usuário

## História de Usuário 1: Cadastro de Aluno
**Como** um aluno,  
**Eu quero** me cadastrar no sistema,  
**Para que** eu possa participar do programa de mérito e receber moedas.

### Critérios de Aceitação:
- O cadastro deve solicitar nome, email, CPF, RG, endereço, instituição de ensino e curso.
- As instituições já devem estar cadastradas no sistema para que o aluno escolha uma.
- O sistema deve confirmar o cadastro via email.

---

## História de Usuário 2: Cadastro de Empresa Parceira
**Como** uma empresa parceira,  
**Eu quero** me cadastrar no sistema,  
**Para que** eu possa oferecer vantagens aos alunos em troca de moedas.

### Critérios de Aceitação:
- O cadastro deve solicitar nome da empresa, CNPJ, email, e uma descrição das vantagens oferecidas.
- A empresa deve poder cadastrar vantagens, indicando o custo em moedas, descrição, e incluir uma imagem do produto.

---

## História de Usuário 3: Envio de Moedas pelo Professor
**Como** um professor,  
**Eu quero** enviar moedas para um aluno,  
**Para que** eu possa recompensar o bom comportamento ou participação em sala de aula.

### Critérios de Aceitação:
- O professor deve possuir saldo suficiente de moedas.
- O envio de moedas deve solicitar o aluno, a quantidade e um motivo obrigatório (mensagem).
- O saldo de moedas do professor deve ser atualizado.
- O aluno deve ser notificado via email quando receber moedas.

---

## História de Usuário 4: Troca de Moedas por Vantagens
**Como** um aluno,  
**Eu quero** trocar minhas moedas por vantagens,  
**Para que** eu possa aproveitar descontos ou adquirir materiais específicos.

### Critérios de Aceitação:
- O aluno deve poder selecionar uma vantagem e confirmar a troca.
- O saldo de moedas do aluno deve ser atualizado automaticamente.
- Um email com um código de cupom deve ser enviado ao aluno.
- O parceiro responsável pela vantagem deve ser notificado via email com o código de conferência.

---

## História de Usuário 5: Consulta de Extrato
**Como** um usuário (aluno ou professor),  
**Eu quero** consultar o meu extrato de transações,  
**Para que** eu possa ver o total de moedas e as transações realizadas.

### Critérios de Aceitação:
- O usuário deve poder visualizar seu saldo atual de moedas.
- O extrato deve exibir as transações de envio/recebimento de moedas, incluindo datas, valores e motivos.

---

## História de Usuário 6: Autenticação de Usuário
**Como** um usuário (aluno, professor ou empresa),  
**Eu quero** realizar login no sistema,  
**Para que** eu possa acessar as funcionalidades conforme meu perfil.

### Critérios de Aceitação:
- O login deve exigir um email e senha válidos.
- Apenas usuários autenticados podem realizar operações no sistema.
- Um processo de recuperação de senha deve estar disponível.
