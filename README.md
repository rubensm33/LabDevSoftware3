# Histórias de Usuário para o Sistema de Gestão de Aluguéis de Automóveis

## História de Usuário 1: Cadastro de Cliente
**Como** um cliente,  
**Eu quero** me cadastrar no sistema,  
**Para que** eu possa realizar reservas de veículos.

### Critérios de Aceitação:
- O cadastro deve solicitar nome completo, email, telefone, CPF, data de nascimento e endereço.
- O sistema deve enviar uma confirmação de cadastro via email.
  
---

## História de Usuário 2: Consulta de Veículos Disponíveis
**Como** um cliente,  
**Eu quero** consultar os veículos disponíveis para aluguel,  
**Para que** eu possa escolher o carro que melhor atende às minhas necessidades.

### Critérios de Aceitação:
- O cliente deve poder filtrar os veículos por categoria (econômico, SUV, luxo), preço e data de disponibilidade.
- A lista de veículos deve incluir nome do modelo, ano, categoria e preço diário de aluguel.

---

## História de Usuário 3: Realizar Reserva de Veículo
**Como** um cliente,  
**Eu quero** reservar um veículo,  
**Para que** eu possa garantir a disponibilidade do carro desejado para as datas de minha viagem.

### Critérios de Aceitação:
- A reserva deve permitir a escolha de data de início e término do aluguel.
- O sistema deve calcular automaticamente o valor total da reserva com base nos dias e no preço do veículo.
- O cliente deve receber um email de confirmação da reserva.

---

## História de Usuário 4: Gerenciar Frota de Veículos
**Como** um administrador,  
**Eu quero** gerenciar a frota de veículos,  
**Para que** eu possa adicionar, remover ou editar as informações de cada carro.

### Critérios de Aceitação:
- O administrador deve poder cadastrar novos veículos, informando modelo, ano, categoria, placa, e status (disponível ou em manutenção).
- O administrador deve poder editar ou remover veículos do sistema.
- O status de cada veículo deve ser atualizado automaticamente quando o carro for reservado ou devolvido.

---

## História de Usuário 5: Pagamento de Reserva
**Como** um cliente,  
**Eu quero** realizar o pagamento de minha reserva online,  
**Para que** eu possa garantir o aluguel do veículo de forma segura e rápida.

### Critérios de Aceitação:
- O cliente deve poder escolher entre diferentes formas de pagamento (cartão de crédito, boleto, etc.).
- O sistema deve processar o pagamento e atualizar o status da reserva para "paga".
- Um recibo deve ser enviado por email após a confirmação do pagamento.

---

## História de Usuário 6: Relatório de Aluguéis
**Como** um administrador,  
**Eu quero** visualizar relatórios de aluguéis,  
**Para que** eu possa monitorar o desempenho do negócio e a utilização da frota.

### Critérios de Aceitação:
- O relatório deve exibir informações como total de aluguéis por período, receitas geradas, e utilização de cada veículo.
- O relatório deve ser exportável em formatos como PDF ou Excel.

---

## História de Usuário 7: Devolução de Veículo
**Como** um cliente,  
**Eu quero** devolver o veículo no final do aluguel,  
**Para que** o sistema possa registrar o término do meu contrato de aluguel.

### Critérios de Aceitação:
- O cliente deve poder informar a data e hora de devolução.
- O sistema deve calcular se há algum valor adicional devido a devolução tardia e atualizar o pagamento final.
- O status do veículo deve ser alterado para "disponível" após a devolução.
