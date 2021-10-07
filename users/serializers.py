from shopifyapp.main import ma

class MasterDBSchema(ma.Schema):
    class Meta:
        fields = ("id", "shopURL", "firstName", "lastName", "adminEmail")




user_schema = MasterDBSchema()
users_schema = MasterDBSchema(many=True)