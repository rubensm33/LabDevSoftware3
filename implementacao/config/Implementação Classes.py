from datetime import datetime
import uuid

class Usuario:
    def __init__(self, nome, email, cpf, login, senha):
        self.nome = nome
        self.email = email
        self.cpf = cpf
        self.login = login
        self.senha = senha

class Aluno(Usuario):
    def __init__(self, nome, email, cpf, rg, endereco, instituicao, curso, login, senha):
        super().__init__(nome, email, cpf, login, senha)
        self.rg = rg
        self.endereco = endereco
        self.instituicao = instituicao
        self.curso = curso
        self.saldo_moedas = 0
        self.extrato = []

    def receber_moedas(self, quantidade, motivo, professor):
        if quantidade > 0:
            transacao = Transacao(quantidade, "recebimento", motivo, professor.nome)
            self.extrato.append(transacao)
            self.saldo_moedas += quantidade
            print(f"Notificação: {self.nome} recebeu {quantidade} moedas de {professor.nome} por: {motivo}")

        else:
            print("Quantidade inválida para recebimento.")

    def trocar_moedas(self, vantagem):
        if self.saldo_moedas >= vantagem.custo:
            self.saldo_moedas -= vantagem.custo
            transacao = Transacao(vantagem.custo, "troca", f"Resgate de vantagem: {vantagem.descricao}", self.nome)
            self.extrato.append(transacao)
            print(f"Notificação: {self.nome} resgatou a vantagem {vantagem.descricao}. Cupom enviado.")
         
        else:
            print("Saldo insuficiente para troca.")

    def consultar_extrato(self):
        print(f"Extrato de {self.nome}:")
        for transacao in self.extrato:
            print(transacao)

class Professor(Usuario):
    def __init__(self, nome, email, cpf, departamento, instituicao, login, senha):
        super().__init__(nome, email, cpf, login, senha)
        self.departamento = departamento
        self.instituicao = instituicao
        self.saldo_moedas = 1000
        self.extrato = []

    def enviar_moedas(self, aluno, quantidade, motivo):
        if self.saldo_moedas >= quantidade and quantidade > 0:
            aluno.receber_moedas(quantidade, motivo, self)
            transacao = Transacao(quantidade, "envio", motivo, aluno.nome)
            self.extrato.append(transacao)
            self.saldo_moedas -= quantidade
        else:
            print("Saldo insuficiente ou quantidade inválida para envio.")

    def consultar_extrato(self):
        print(f"Extrato de {self.nome}:")
        for transacao in self.extrato:
            print(transacao)

class EmpresaParceira(Usuario):
    def __init__(self, nome, email, cpf, login, senha):
        super().__init__(nome, email, cpf, login, senha)
        self.vantagens = []

    def cadastrar_vantagem(self, descricao, custo, foto):
        vantagem = Vantagem(descricao, custo, foto)
        self.vantagens.append(vantagem)

class Transacao:
    def __init__(self, quantidade, tipo, motivo, participante):
        self.id = uuid.uuid4()
        self.quantidade = quantidade
        self.tipo = tipo
        self.motivo = motivo
        self.participante = participante
        self.data = datetime.now()

    def __str__(self):
        return f"{self.data} - {self.tipo.capitalize()} de {self.quantidade} moedas para {self.participante}. Motivo: {self.motivo}"

class Vantagem:
    def __init__(self, descricao, custo, foto):
        self.descricao = descricao
        self.custo = custo
        self.foto = foto

class SistemaMerito:
    def __init__(self):
        self.alunos = {}
        self.professores = {}
        self.empresas = {}

    def cadastrar_aluno(self, nome, email, cpf, rg, endereco, instituicao, curso, login, senha):
        aluno = Aluno(nome, email, cpf, rg, endereco, instituicao, curso, login, senha)
        self.alunos[cpf] = aluno

    def cadastrar_professor(self, nome, email, cpf, departamento, instituicao, login, senha):
        professor = Professor(nome, email, cpf, departamento, instituicao, login, senha)
        self.professores[cpf] = professor

    def cadastrar_empresa(self, nome, email, cpf, login, senha):
        empresa = EmpresaParceira(nome, email, cpf, login, senha)
        self.empresas[cpf] = empresa

    def buscar_aluno(self, cpf):
        return self.alunos.get(cpf)

    def buscar_professor(self, cpf):
        return self.professores.get(cpf)

    def buscar_empresa(self, cpf):
        return self.empresas.get(cpf)
