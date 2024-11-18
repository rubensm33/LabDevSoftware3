from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

from controller import  token, aluno, transacao, professor, instituicao, empresa, user

app = FastAPI()

app.include_router(token.router, tags=["Autenticação"])
app.include_router(aluno.router, tags=["Alunos"])
app.include_router(transacao.router, tags=["Transações"])
app.include_router(professor.router, tags=["Professores"])
app.include_router(instituicao.router, tags=["Instituições"])
app.include_router(empresa.router, tags=["Empresas"])
app.include_router(user.router, tags=["Users"])
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
