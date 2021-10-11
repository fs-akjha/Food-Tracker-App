from flask.json import jsonify
from sqlalchemy.orm import session
from sqlalchemy.sql.expression import select
from sqlalchemy.sql.functions import count, mode
from shopifyapp import models
from shopifyapp.main.base import Session
from sqlalchemy import func,select
import mysql.connector


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



class ChildDAO:
        
    def create_new_token(self,clientID,shopURL,accessToken,shopName,validity):
        ext_db=mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="{}".format(shopName.lower())
        )
        mycursor=ext_db.cursor()
        query="Insert into tokens(clientID,shopURL,accessToken,validity) values({},'{}','{}','{}')".format(clientID,shopURL,accessToken,validity)
        mycursor.execute(query)
        ext_db.commit()
        ext_db.close()
        return "200"

    def create_reward_points(self,customerID,customerEmail,orderNo,orderValue,campaignID,pointsRewarded,status,dateCreated,shopName):
        ext_db=mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="{}".format(shopName.lower())
        )
        mycursor=ext_db.cursor()
        query="Insert into reward_points(customerID,customerEmail,orderNo,orderValue,campaignID,pointsRewarded,status,dateCreated) values({},'{}',{},{},{},{},'{}','{}')".format(customerID,customerEmail,orderNo,orderValue,campaignID,pointsRewarded,status,dateCreated)
        mycursor.execute(query)
        ext_db.commit()
        ext_db.close()
        return "200"

    def get_all_tokens(self,shopName):
        ext_db=mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="{}".format(shopName.lower())
        )
        mycursor=ext_db.cursor()
        query="SELECT * FROM tokens"
        mycursor.execute(query)
        columns = mycursor.description
        result = []
        for value in mycursor.fetchall():
                tmp = {}
                for (index,column) in enumerate(value):
                    tmp[columns[index][0]] = column
                result.append(tmp)
        ext_db.close()
        return result

    def get_all_reward_points(self,shopName):
        ext_db=mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="{}".format(shopName.lower())
        )
        mycursor=ext_db.cursor()
        query="SELECT * FROM reward_points"
        mycursor.execute(query)
        columns = mycursor.description
        result = []
        for value in mycursor.fetchall():
                tmp = {}
                for (index,column) in enumerate(value):
                    tmp[columns[index][0]] = column
                result.append(tmp)
        ext_db.close()
        return result

    def list_tokens_byid(self,shopName,clientID):
        ext_db=mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="{}".format(shopName.lower())
        )
        mycursor=ext_db.cursor()
        query="SELECT * FROM tokens where clientID in ({})".format(clientID)
        mycursor.execute(query)
        columns = mycursor.description
        result = []
        for value in mycursor.fetchall():
                tmp = {}
                for (index,column) in enumerate(value):
                    tmp[columns[index][0]] = column
                result.append(tmp)
        ext_db.close()
        return result

    def list_rewardpoints_byid(self,shopName,customerID):
        ext_db=mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="{}".format(shopName.lower())
        )
        mycursor=ext_db.cursor()
        query="SELECT * FROM reward_points where customerID in ({})".format(customerID)
        mycursor.execute(query)
        columns = mycursor.description
        result = []
        for value in mycursor.fetchall():
                tmp = {}
                for (index,column) in enumerate(value):
                    tmp[columns[index][0]] = column
                result.append(tmp)
        ext_db.close()
        return result


child_dao=ChildDAO()
user_dao = UserDAO(models.Clients)