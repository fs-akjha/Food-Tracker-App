from .serializers import plans_schema
from persistance.users_dao import linkedintokens_dao
import mysql.connector
from flask import jsonify
from datetime import datetime
import datetime
import requests
import time
import time
from datetime import date
import io
import json
from users import app

class UserService:

    def __init__(self):
        self.db=mysql.connector.connect
        self.host=app.config['HOST']
        self.user=app.config['USER']
        self.password=app.config['PASSWORD']

    def creating_new_token(self,shopurl,CLIENT_ID,shopName,params):
        ts = time.time()
        try:
            import datetime
            validity=datetime.datetime.today() + datetime.timedelta(days=1)
            result = user_service.list_users_byshopurl_length(shopurl)
            print("ksnnksdkskd",result)
            print(result)
            if(result<1):
                clientID=CLIENT_ID
                resp = requests.post("https://{}.myshopify.com/admin/oauth/access_token".format(shopName),data=params)
                result=resp.json()
                print(resp)
                access_token_value=result["access_token"]
                shop_url='https://{}/admin/api/2021-10/shop.json'.format(shopurl)
                accessToken=access_token_value
                shop_details=requests.get(shop_url,headers={'X-Shopify-Access-Token':access_token_value})
                shop_url='https://{}.myshopify.com/admin/api/2021-10/shop.json'.format(shopName)
                r=requests.get(shop_url,headers={'X-Shopify-Access-Token':accessToken})
                shop_data=r.json()
                datas=shop_data['shop']
                shopURL=shopurl
                firstName=datas['shop_owner']
                adminEmail=datas['email']
                paymentEnableStatus=str(datas['eligible_for_payments'])
                subscriptionPlanID='Trial'
                validityDate=datetime.datetime.utcnow()
                dateCreated=datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
                result=user_service.create_user(shopURL,firstName,adminEmail,paymentEnableStatus,subscriptionPlanID,validityDate,dateCreated,shopName)
                results=user_service.create_token(clientID,shopurl,accessToken,shopName,validity)
                token_details=user_service.list_all_tokens(shopName)
                return token_details,200
            else:
                pass
        except:
            return{"Message":"Either Code Value is Incorrect or Shop Name is Wrong","status":0},400

    def updating_existing_token(self,CLIENT_ID,shopName,params):
        try:
            import datetime
            try:
                user_service.create_user_after_deletion(shopName)
            except:
                print("Database Already There")
            clientID=CLIENT_ID
            result = user_service.list_validty_tokens(shopName)
            token_length=user_service.get_all_tokens_length(shopName)
            statu=result['status']
            val=0
            for i in statu:
                val=i['validity']
            valid_date=val
            current_date=datetime.date.today()
            print("Yes In Updating Token Part")
            if valid_date<=current_date:
                resp = requests.post("https://{}.myshopify.com/admin/oauth/access_token".format(shopName),data=params)
                result=resp.json()
                access_token_value=result["access_token"]
                accessToken=access_token_value
                print("Updated Access Token Value:- ",accessToken)
                shopURL='{}.myshopify.com'.format(shopName)
                validity_date=datetime.datetime.today() + datetime.timedelta(days=1)
                results=user_service.update_token(shopURL,accessToken,shopName,validity_date)
                return jsonify(user_service.list_tokens_byid(shopName,clientID))
            elif(token_length>=1 or token_length==0):
                resp = requests.post("https://{}.myshopify.com/admin/oauth/access_token".format(shopName),data=params)
                result=resp.json()
                access_token_value=result["access_token"]
                accessToken=access_token_value
                print("Updated Access Token Value:- ",accessToken)
                shopURL='{}.myshopify.com'.format(shopName)
                validityDate=datetime.datetime.utcnow()
                status=1
                user_service.update_client_status(shopName,validityDate,status)
                validity_date=datetime.datetime.today() + datetime.timedelta(days=1)
                results=user_service.update_token(shopURL,accessToken,shopName,validity_date)
                return jsonify(user_service.list_tokens_byid(shopName,clientID))
            else:
                clientID=CLIENT_ID
                return jsonify(user_service.list_tokens_byid(shopName,clientID))
        except:
            return{"Message":"Kindly give the Correct Code Value if updating the existing Access Token","status":0},400
    

    def add_plans(self,cat_id,name,icon,cost,caption,dateCreated,plan_data):
        create_plans = linkedintokens_dao.add_tokens(cat_id,name,icon,cost,caption,dateCreated,plan_data)
        return {"status":create_plans}

    def get_plan_detail_byid(self,id):
        token=linkedintokens_dao.get_plan_detail_byid(id)
        result = plans_schema.dump(token)
        return ({'users':result})

    def get_plan_detail(self):
        all_users = linkedintokens_dao.get_plan_detail()
        result = plans_schema.dump(all_users)
        return ({'users':result})

    def list_users_byplanname_length(self,name):
        token=linkedintokens_dao.list_users_byplanname_length(name)
        result = plans_schema.dump(token)
        length_result=len(result)
        return length_result

user_service = UserService()