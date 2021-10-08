from .serializers import user_schema, users_schema
from persistance.users_dao import user_dao
import mysql.connector

class UserService:

    def list_users(self):
        all_users = user_dao.get_all()
        result = users_schema.dump(all_users)
        return ({'users':result})

    def create_user(self,shopURL,firstName,lastName,adminEmail,adminPhone,paymentEnableStatus,subscriptionMode,subscriptionPlanID,validityDate,dateCreated,status,shopName):
        create_user = user_dao.create_new_user(shopURL,firstName,lastName,adminEmail,adminPhone,paymentEnableStatus,subscriptionMode,subscriptionPlanID,validityDate,dateCreated,status,shopName)
        db=mysql.connector.connect(
            host="localhost",
            user="root",
            password="root"
        )
        mycursor=db.cursor()
        mycursor.execute("CREATE DATABASE {}".format(shopName))
        new_db=mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="{}".format(shopName.lower())
        )
        my_new_cursor=new_db.cursor()
        my_new_cursor.execute("CREATE TABLE Tokens (id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,clientID INTEGER(10) NOT NULL, shopURL VARCHAR(150) NOT NULL, accessToken VARCHAR(255) NOT NULL, validity date NOT NULL)")
        my_new_cursor.execute("CREATE TABLE Reward_Points (id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,customerID INTEGER(10), customerEmail VARCHAR(150) NOT NULL, orderNo INTEGER NOT NULL, orderValue INTEGER NOT NULL, campaignID INTEGER NOT NULL,pointsRewarded INTEGER NOT NULL,status enum('M','F') NOT NULL, dateCreated date NOT NULL)")
        my_new_cursor.execute("CREATE TABLE Total_Points (id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,customerID INTEGER(10), customerEmail VARCHAR(150), totalPointsEarned INTEGER NOT NULL, totalPointsRedeemed INTEGER NOT NULL, totalPoints INTEGER NOT NULL, dateUpdated date NOT NULL)")
        my_new_cursor.execute("CREATE TABLE Redeem_History (id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,customerID INTEGER(10), customerEmail VARCHAR(150), orderNo INTEGER NOT NULL, orderValue INTEGER NOT NULL, campaignID INTEGER NOT NULL, pointsUsed INTEGER NOT NULL, equivalentValue INTEGER NOT NULL, status enum('M','F') NOT NULL, dateCreated date NOT NULL)")
        return {"status":create_user}

user_service = UserService()