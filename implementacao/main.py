from fastapi import FastAPI
import uvicorn

from controller import user, token, aluno, transacao, professor, instituicao, empresa


app = FastAPI()
# app.include_router(user.router)
app.include_router(token.router)
app.include_router(aluno.router)
app.include_router(transacao.router)
app.include_router(professor.router)
app.include_router(instituicao.router)
app.include_router(empresa.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
