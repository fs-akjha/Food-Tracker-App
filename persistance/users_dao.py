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

    def get_plan_detail_byid(self, id):
        session = Session()
        result =  (
            session.query(self.model)
                .filter_by(created_by_user_id=id)
        )
        session.close()
        return result

    def get_plan_detail(self):
        session = Session()
        result = session.query(self.model).all()
        session.close()
        return result

    def list_users_byplanname_length(self, name):
        session = Session()
        result =  (
            session.query(self.model)
                .filter_by(name=name)
        )
        session.close()
        return result

linkedintokens_dao=LinkedinTokens(models.LinkedinTokens)