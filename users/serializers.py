from fsconnectapp.main import ma

class PlanSchema(ma.Schema):
    class Meta:
        fields=("id","clientID","accessToken","refresh_accessToken","validityDate","refresh_token_validityDate","dateCreated")

linkedintokens_schema = PlanSchema()
linkedintokens_schema = PlanSchema(many=True)