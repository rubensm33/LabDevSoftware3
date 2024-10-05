from pydantic import BaseModel


class Scope(BaseModel):
    scope: str | None = None

    class Config:
        orm_mode = True