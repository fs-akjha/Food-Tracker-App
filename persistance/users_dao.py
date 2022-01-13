from flask.json import jsonify
from sqlalchemy.orm import session
from sqlalchemy.sql.expression import select
from sqlalchemy.sql.functions import count, mode
from fsconnectapp import models
from fsconnectapp.main.base import Session
from sqlalchemy import func,select
import mysql.connector
from persistance import app


class LinkedinTokens:
    def __init__(self, model):
        self.model = model

    def add_tokens(self,cat_id,name,icon,cost,caption,dateCreated,plan_data):
        session = Session()
        new_category = self.model(category_id=cat_id,name=name,icon=icon,cost=cost,caption=caption,dateCreated=dateCreated,plan_data=plan_data)
        session.add(new_category)
        session.commit()
        session.close()
        return "200"

    def list_all_tokens(self, clientID):
        session = Session()
        result =  (
            session.query(self.model)
                .filter_by(clientID=clientID)
        )
        session.close()
        return result

    def get_plan_detail(self):
        session = Session()
        result = session.query(self.model).all()
        session.close()
        return result

    def list_users_byclientid(self, clientID):
        session = Session()
        result =  (
            session.query(self.model)
                .filter_by(clientID=clientID)
        )
        session.close()
        return result
    
    def create_new_user(self,clientID,accessToken,validityDate,dateCreated):
        session = Session()
        new_user = self.model(clientID=clientID,accessToken=accessToken,validityDate=validityDate,dateCreated=dateCreated)
        session.add(new_user)
        session.commit()
        session.close()
        return "200"

linkedintokens_dao=LinkedinTokens(models.LinkedinTokens)