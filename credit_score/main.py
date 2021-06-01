# uvicorn main:app --reload
# http://127.0.0.1:8000/docs
#uvicorn credit_score.main:app --reload

import json
from fastapi import FastAPI, Depends, Body
from credit_score.apps.score.score import Score
from fastapi.responses import JSONResponse
from credit_score.apps.score.entities.user_entity_schema import UserSchema, UserLoginSchema, ResponseScore,UserEntitySchemaPydantic, UserEntitySchema
from credit_score.apps.core.auth.auth_handler import signJWT
from credit_score.apps.core.auth.auth_bearer import JWTBearer


app = FastAPI(title="Credit Score API",
    description="Api que retorna o score de pessoas para a mesa de crédito",
    version="0.3")


@app.post("/login", tags=["Autenticação"])
async def user_login(user: UserLoginSchema):
    usuario = UserSchema()
    if usuario.user == user.user and usuario.password==user.password:
        return signJWT(user.user)
    else:
        return {"error": "Usuário e/ou senha inválidos"}


@app.post("/score", dependencies=[Depends(JWTBearer())] , tags=["Cálculo Score"], response_model= ResponseScore)
async def retorna_score(score_data: UserEntitySchemaPydantic):
    
    #faz qqlr coisa
    
    return {'hello':'world'}
