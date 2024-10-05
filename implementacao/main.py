from fastapi import FastAPI
import uvicorn

from controller import user, token


app = FastAPI()
app.include_router(user.router)
app.include_router(token.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
