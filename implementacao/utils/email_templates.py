def email_compra_template(codigo):
    return f"""
    <html>
    <body>
        <h1>Parabéns pela compra!</h1>
        <p>Você adquiriu a vantagem com sucesso. Aqui está seu código:</p>
        <h2>{codigo}</h2>
        <p>Use esse código para aproveitar sua vantagem.</p>
    </body>
    </html>
    """


def email_notificacao_empresa(aluno_nome, vantagem_descricao, codigo):
    return f"""
    <html>
    <body>
        <h1>Nova Compra Realizada</h1>
        <p>O aluno <strong>{aluno_nome}</strong> realizou a compra da seguinte vantagem:</p>
        <h2>{vantagem_descricao}</h2>
        <p>Código gerado: <strong>{codigo}</strong></p>
    </body>
    </html>
    """


def email_professor_moedas(professor_nome, valor, motivo):
    return f"""
    <html>
    <body>
        <h1>Você recebeu moedas!</h1>
        <p>O professor <strong>{professor_nome}</strong> enviou <strong>{valor} moedas</strong> para você.</p>
        <p>Motivo: {motivo}</p>
        <p>Aproveite para utilizá-las na plataforma!</p>
    </body>
    </html>
    """
