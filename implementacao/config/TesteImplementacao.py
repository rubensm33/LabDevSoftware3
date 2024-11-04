import unittest

class SistemaMeritoTests(unittest.TestCase):
    def setUp(self):
   
        self.sistema = SistemaMerito()
        self.sistema.cadastrar_professor(
            nome="Professor Carlos", email="carlos@universidade.com", cpf="11111111111", 
            departamento="Matemática", instituicao="Universidade A", login="prof.carlos", senha="1234"
        )
        self.sistema.cadastrar_aluno(
            nome="Aluno João", email="joao@aluno.com", cpf="22222222222", rg="3333333", 
            endereco="Rua A, 123", instituicao="Universidade A", curso="Engenharia", 
            login="aluno.joao", senha="abcd"
        )
        self.sistema.cadastrar_empresa(
            nome="Empresa X", email="contato@empresax.com", cpf="44444444444", 
            login="empresa.x", senha="empresa123"
        )
        
        self.aluno = self.sistema.buscar_aluno("22222222222")
        self.professor = self.sistema.buscar_professor("11111111111")
        self.empresa = self.sistema.buscar_empresa("44444444444")

    def test_envio_moedas(self):
        
        self.professor.enviar_moedas(self.aluno, 100, "Bom comportamento")
        self.assertEqual(self.professor.saldo_moedas, 900, "Saldo do professor deve ser 900 após envio")
        self.assertEqual(self.aluno.saldo_moedas, 100, "Saldo do aluno deve ser 100 após receber moedas")
        
    def test_extrato_professor(self):
        
        self.professor.enviar_moedas(self.aluno, 50, "Participação ativa")
        extrato_professor = [str(transacao) for transacao in self.professor.extrato]
        self.assertTrue("envio de 50 moedas" in extrato_professor[0].lower(), "Extrato do professor deve registrar o envio")

    def test_extrato_aluno(self):
       
        self.professor.enviar_moedas(self.aluno, 50, "Participação ativa")
        extrato_aluno = [str(transacao) for transacao in self.aluno.extrato]
        self.assertTrue("recebimento de 50 moedas" in extrato_aluno[0].lower(), "Extrato do aluno deve registrar o recebimento")
    
    def test_troca_moedas(self):
        
        vantagem = Vantagem("Desconto em restaurante", 50, "foto.jpg")
        self.empresa.cadastrar_vantagem(vantagem.descricao, vantagem.custo, vantagem.foto)
        
        
        self.professor.enviar_moedas(self.aluno, 50, "Participação")
        
        self.aluno.trocar_moedas(vantagem)
        
       
        self.assertEqual(self.aluno.saldo_moedas, 0, "Saldo do aluno deve ser 0 após troca")
        extrato_aluno = [str(transacao) for transacao in self.aluno.extrato]
        self.assertTrue("resgate de vantagem: desconto em restaurante" in extrato_aluno[1].lower(), "Extrato do aluno deve registrar a troca")

if __name__ == "__main__":
    unittest.main()
