# uvicorn main:app --reload
# http://127.0.0.1:8000/docs
#uvicorn credit_score.main:app --reload

import json
from fastapi import FastAPI, Depends, Body

from fastapi.responses import JSONResponse
from credit_score.apps.entities.user_entity_schema import ResponseScore, UserEntitySchemaPydantic


app = FastAPI(title="Credit Score API",
    description="Api que retorna o score de pessoas para a mesa de crédito",
    version="0.3")
    

@app.post("/score", tags=["Cálculo Score"], response_model= ResponseScore)
async def retorna_score(score_data: UserEntitySchemaPydantic):
    
    #faz qqlr coisa
    
    return {'hello':'world'}
