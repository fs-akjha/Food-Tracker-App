from .serializers import user_schema, users_schema
from persistance.users_dao import user_dao,child_dao
import mysql.connector

class UserService:

    def list_users(self):
        all_users = user_dao.get_all()
        result = users_schema.dump(all_users)
        return ({'users':result})

    def list_all_tokens(self,shopName):
        all_tokens=child_dao.get_all_tokens(shopName)
        return {"status":all_tokens}

    def list_all_rward_points(self,shopName):
        all_tokens=child_dao.get_all_reward_points(shopName)
        return {"status":all_tokens}

    def list_total_rward_points(self,shopName):
        all_tokens=child_dao.list_total_reward_points(shopName)
        return {"status":all_tokens}

    def list_total_redeem_history_data(self,shopName):
        all_tokens=child_dao.list_total_redeem_history_data(shopName)
        return {"status":all_tokens}

    def list_tokens_byid(self,shopName,clientID):
        all_tokens=child_dao.list_tokens_byid(shopName,clientID)
        return {"status":all_tokens}

    def list_rewardpoints_byid(self,shopName,customerID):
        all_tokens=child_dao.list_rewardpoints_byid(shopName,customerID)
        return {"status":all_tokens}

    def list_totalpoints_byid(self,shopName,customerID):
        all_tokens=child_dao.list_totalpoints_byid(shopName,customerID)
        return {"status":all_tokens}

    def list_redeemhistory_data_byid(self,shopName,customerID):
        all_tokens=child_dao.list_redeemhistory_data_byid(shopName,customerID)
        return {"status":all_tokens}

    def list_rewardpoints_bymail(self,shopName,customerEmail):
        all_tokens=child_dao.list_rewardpoints_bymail(shopName,customerEmail)
        return {"status":all_tokens}

    def list_totalpoints_bymail(self,shopName,customerEmail):
        all_tokens=child_dao.list_totalpoints_bymail(shopName,customerEmail)
        return {"status":all_tokens}

    def list_redeemhistory_data_bymail(self,shopName,customerEmail):
        all_tokens=child_dao.list_redeemhistory_data_bymail(shopName,customerEmail)
        return {"status":all_tokens}

    def create_token(self,clientID,shopURL,accessToken,shopName,validity):
        data=child_dao.create_new_token(clientID,shopURL,accessToken,shopName,validity)
        return {"status":data}

    def create_reward_points(self,customerID,customerEmail,orderNo,orderValue,campaignID,pointsRewarded,status,dateCreated,shopName):
        data=child_dao.create_reward_points(customerID,customerEmail,orderNo,orderValue,campaignID,pointsRewarded,status,dateCreated,shopName)
        return {"status":data}

    def create_total_points(self,customerID,customerEmail,totalPointsEarned,totalPointsRedeemed,totalPoints,dateUpdated,shopName):
        data=child_dao.create_total_points(customerID,customerEmail,totalPointsEarned,totalPointsRedeemed,totalPoints,dateUpdated,shopName)
        return {"status":data}

    def create_redeem_history_points(self,customerID,customerEmail,orderNo,orderValue,campaignID,pointsUsed,equivalentValue,status,shopName,dateCreated):
        data=child_dao.create_redeem_history_points(customerID,customerEmail,orderNo,orderValue,campaignID,pointsUsed,equivalentValue,status,shopName,dateCreated)
        return {"status":data}

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
        my_new_cursor.execute("CREATE TABLE Reward_Points (id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,customerID INTEGER(10) NOT NULL, customerEmail VARCHAR(150) NOT NULL, orderNo INTEGER NOT NULL, orderValue INTEGER NOT NULL, campaignID INTEGER NOT NULL,pointsRewarded INTEGER NOT NULL,status enum('T','F') NOT NULL, dateCreated date NOT NULL)")
        my_new_cursor.execute("CREATE TABLE Total_Points (id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,customerID INTEGER(10) NOT NULL, customerEmail VARCHAR(150) NOT NULL, totalPointsEarned INTEGER NOT NULL, totalPointsRedeemed INTEGER NOT NULL, totalPoints INTEGER NOT NULL, dateUpdated datetime NOT NULL)")
        my_new_cursor.execute("CREATE TABLE Redeem_History (id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,customerID INTEGER(10) NOT NULL, customerEmail VARCHAR(150) NOT NULL, orderNo INTEGER NOT NULL, orderValue INTEGER NOT NULL, campaignID INTEGER NOT NULL, pointsUsed INTEGER NOT NULL, equivalentValue INTEGER NOT NULL, status enum('T','F') NOT NULL, dateCreated datetime NOT NULL)")
        return {"status":create_user}

user_service = UserService()