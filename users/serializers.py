from fsconnectapp.main import ma

class PlanSchema(ma.Schema):
    class Meta:
        fields=("id","clientID","accessToken","validityDate","dateCreated")

linkedintokens_schema = PlanSchema()
linkedintokens_schema = PlanSchema(many=True)