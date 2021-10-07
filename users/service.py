from .serializers import user_schema, users_schema
from persistance.users_dao import user_dao

class UserService:

    def list_users(self):
        all_users = user_dao.get_all()
        result = users_schema.dump(all_users)
        return ({'users':result})

    def create_user(self,shopURL,firstName,lastName,adminEmail,adminPhone,paymentEnableStatus,subscriptionMode,subscriptionPlanID,validityDate,dateCreated,status,shopName):
        create_user = user_dao.create_new_user(shopURL,firstName,lastName,adminEmail,adminPhone,paymentEnableStatus,subscriptionMode,subscriptionPlanID,validityDate,dateCreated,status,shopName)
        return {"status":create_user}



user_service = UserService()