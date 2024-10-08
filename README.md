# Histórias de Usuário - Sistema de Mérito Estudantil

## 1. Cadastrar Aluno
   - **Como** aluno,
   - **Eu quero** me cadastrar no sistema com meus dados pessoais (nome, CPF, e-mail, curso),
   - **Para que** eu possa acessar o sistema e participar do programa de mérito estudantil.

   ### Critérios de Aceitação:
   - O aluno deve fornecer todos os dados obrigatórios para se cadastrar.
   - O sistema deve validar o CPF para garantir que é único.
   - O aluno receberá um e-mail de confirmação após o cadastro.

---

## 2. Consultar Extrato
   - **Como** aluno,
   - **Eu quero** consultar o meu extrato de transações de moedas,
   - **Para que** eu possa verificar as moedas recebidas e gastas no sistema.

   ### Critérios de Aceitação:
   - O extrato deve exibir todas as transações realizadas com detalhes como data, valor, e motivo.
   - O saldo de moedas deve ser atualizado após cada transação.

---

## 3. Trocar Moedas por Vantagens
   - **Como** aluno,
   - **Eu quero** trocar minhas moedas por vantagens oferecidas pelas empresas parceiras,
   - **Para que** eu possa usufruir dos benefícios do programa.

   ### Critérios de Aceitação:
   - O aluno pode visualizar uma lista de vantagens disponíveis com o custo em moedas.
   - O sistema deve validar se o aluno tem saldo suficiente para resgatar a vantagem.
   - Após o resgate, o saldo de moedas do aluno é atualizado e ele recebe uma notificação.

---

## 4. Enviar Moedas
   - **Como** professor,
   - **Eu quero** enviar moedas para um aluno como recompensa por seu desempenho acadêmico,
   - **Para que** eu possa incentivar o aluno a continuar seu bom desempenho.

   ### Critérios de Aceitação:
   - O professor deve selecionar o aluno e o motivo pelo qual está enviando as moedas.
   - O saldo de moedas do professor é atualizado após o envio.
   - O aluno recebe uma notificação e o valor aparece no seu extrato.

---

## 5. Cadastrar Vantagens
   - **Como** empresa parceira,
   - **Eu quero** cadastrar vantagens no sistema com o valor correspondente em moedas,
   - **Para que** os alunos possam resgatar as vantagens em troca de suas moedas.

   ### Critérios de Aceitação:
   - A empresa pode adicionar uma nova vantagem com descrição, custo em moedas, e imagem ilustrativa.
   - O sistema deve exibir a vantagem para os alunos disponíveis para resgate.

---

## 6. Gerenciar Empresas Parceiras
   - **Como** administrador,
   - **Eu quero** gerenciar as empresas parceiras cadastradas no sistema,
   - **Para que** eu possa manter o catálogo de vantagens atualizado.

   ### Critérios de Aceitação:
   - O administrador pode adicionar, editar ou remover empresas parceiras.
   - O sistema deve garantir que as empresas ativas estejam visíveis para os alunos.

---

## 7. Autenticar Usuário
   - **Como** usuário (aluno, professor ou empresa),
   - **Eu quero** fazer login no sistema com minhas credenciais,
   - **Para que** eu possa acessar minha conta e realizar as ações permitidas.

   ### Critérios de Aceitação:
   - O sistema deve validar o e-mail e senha do usuário.
   - Caso as credenciais estejam corretas, o usuário é autenticado e redirecionado ao seu painel.
   - Caso contrário, uma mensagem de erro é exibida.

