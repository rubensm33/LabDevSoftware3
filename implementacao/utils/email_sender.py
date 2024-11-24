import requests
from fastapi import HTTPException

MAILTRAP_URL = "https://sandbox.api.mailtrap.io/api/send/3297430"
MAILTRAP_API_TOKEN = "9cb73bd880d3686f500e015ea7cf272e"


def enviar_email(destinatario, assunto, conteudo):
    """
    Envia um e-mail usando o Mailtrap.
    """
    payload = {
        "from": {"email": "no-reply@suaplataforma.com", "name": "Sua Plataforma"},
        "to": [{"email": destinatario}],
        "subject": assunto,
        "html": conteudo,
        "category": "Notificação",
    }
    headers = {"Authorization": f"Bearer {MAILTRAP_API_TOKEN}", "Content-Type": "application/json"}

    response = requests.post(MAILTRAP_URL, headers=headers, json=payload)
    if response.status_code != 200:
        raise HTTPException(status_code=500, detail=f"Erro ao enviar e-mail: {response.text}")