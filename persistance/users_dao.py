from flask.json import jsonify
from sqlalchemy.orm import session
from sqlalchemy.sql.expression import select
from sqlalchemy.sql.functions import count, mode
from shopifyapp import models
from shopifyapp.main.base import Session
from sqlalchemy import func,select



class UserDAO:
    def __init__(self, model):
        self.model = model

    def create_new_user(self,shopURL,firstName,lastName,adminEmail,adminPhone,paymentEnableStatus,subscriptionMode,subscriptionPlanID,validityDate,dateCreated,status,shopName):
        session = Session()
        new_user = self.model(shopURL=shopURL,firstName=firstName,lastName=lastName,adminEmail=adminEmail,adminPhone=adminPhone,paymentEnableStatus=paymentEnableStatus,subscriptionMode=subscriptionMode,subscriptionPlanID=subscriptionPlanID,validityDate=validityDate,dateCreated=dateCreated,status=status,shopName=shopName)
        session.add(new_user)
        session.commit()
        session.close()
        return "200"

    def get_all(self):
        session = Session()
        result = session.query(self.model).all()
        session.close()
        return result





user_dao = UserDAO(models.Clients)