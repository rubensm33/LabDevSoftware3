from fastapi import FastAPI
import uvicorn

from controller import  token, aluno, transacao, professor, instituicao, empresa

app = FastAPI()

app.include_router(token.router, tags=["Autenticação"])
app.include_router(aluno.router, tags=["Alunos"])
app.include_router(transacao.router, tags=["Transações"])
app.include_router(professor.router, tags=["Professores"])
app.include_router(instituicao.router, tags=["Instituições"])
app.include_router(empresa.router, tags=["Empresas"])

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
