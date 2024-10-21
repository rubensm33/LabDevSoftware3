from fastapi.security import OAuth2PasswordBearer


oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="token",
    scopes={
        "me": "Read information about the current user.",
        "professor": "Professor info",
        "empresa": "Empresa info",
        "aluno": "Aluno info",
    },
)
