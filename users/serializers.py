from fsconnectapp.main import ma

class PlanSchema(ma.Schema):
    class Meta:
        fields=("id","name","icon","created_by_user_id","cost","plan_data","caption","category_id")

plan_schema = PlanSchema()
plans_schema = PlanSchema(many=True)