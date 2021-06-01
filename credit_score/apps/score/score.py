#from credit_score.apps.core.modules.redis import RedisConnection
#from credit_score.apps.core.modules.utils import Util
from credit_score.apps.score.entities.user_entity_schema import (
    UserEntitySchema,
    UserEntitySchemaPydantic,
    UserHistoryEntitySchema,
    UserScoreEntitySchema
)

class Score:
    def __init__(self):
        
        self.user_schema = UserEntitySchema()
        self.user_history_schema = UserHistoryEntitySchema()
        self.user_score_schema = UserScoreEntitySchema()

        #self.redis_client = RedisConnection()

    

    def calcule(self, user_data):   
        #faz qqlr coisa...

        return {"score": 123, "categoria":123}
