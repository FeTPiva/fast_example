#from marshmallow import Schema, fields, post_load, EXCLUDE
#from credit_score.apps.score.entities.user_entity import ScoreEntity, UserEntity, UserHistoryEntity
from pydantic import BaseModel,  Field
from typing import Optional 
from fastapi import Query

class UserEntitySchemaPydantic(BaseModel):

    cpf: str = Query( ...,description="cpf do cliente sem ponto e traço",example='00216827205')
    cd_proposta: int = Query(..., description="código da proposta", example = 123455)
    qtd_dia_embarque: int = Query(..., description="DT_EMBARQUE - DT_PROPOSTA", example = 262) 

    


class ResponseScore(BaseModel):
    score: float  = Query(None, description="Valor de Score do algoritmo",example = 850.15)
    categoria: str = Query(None, description="Categoria: Aprovado, Negado, Cinza",example ="Aprovado")


class UserLoginSchema(BaseModel):
    user: str = Field(...)
    password: str = Field(...)

