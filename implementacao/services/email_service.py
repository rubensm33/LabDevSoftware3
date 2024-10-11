import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from jinja2 import Template


def enviar_email(nome, moedas, faculdade, destinatario):
    servidor_smtp = "smtp.office365.com"
    porta_smtp = 587
    usuario_email = "email@outlook.com"
    senha_email = "senha"

    msg = MIMEMultipart()
    msg["From"] = usuario_email
    msg["To"] = destinatario
    msg["Subject"] = "Recompensa por Bom Comportamento"

    with open("email_template.html", "r") as f:
        template_html = f.read()

    template = Template(template_html)
    mensagem_renderizada = template.render(nome=nome, moedas=moedas, faculdade=faculdade)

    msg.attach(MIMEText(mensagem_renderizada, "html"))

    try:
        servidor = smtplib.SMTP(servidor_smtp, porta_smtp)
        servidor.starttls()
        servidor.login(usuario_email, senha_email)
        servidor.send_message(msg)
        servidor.quit()
        print("E-mail enviado com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")
