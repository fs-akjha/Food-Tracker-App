from calendar import month
from .serializers import linkedintokens_schema
from persistance.users_dao import linkedintokens_dao
import mysql.connector
from flask import jsonify
import requests
import time
import time
from datetime import date
import io
import json
from users import app
from dateutil.relativedelta import *
from datetime import datetime

# access_token=app.config['ACCESS_TOKEN']
# access_token_secret=app.config['ACCESS_TOKEN_SECRET']
# consumer_key=app.config['CONSUMER_KEY']
# consumer_secret=app.config['CONSUMER_SECRET']
# CLIENT_ID=app.config['CLIENT_ID']
# CLIENT_SECRET=app.config['CLIENT_SECRET']

class UserService:

    def __init__(self):
        self.db=mysql.connector.connect
        self.host=app.config['HOST']
        self.user=app.config['USER']
        self.password=app.config['PASSWORD']

    def creating_new_token(self,Auth_code):
        result = user_service.list_users_by_length(clientID=app.config['CLIENT_ID'])
        try:
            if(result<1):
                AUTH_CODE = Auth_code
                ACCESS_TOKEN_URL = 'https://www.linkedin.com/oauth/v2/accessToken'
                redirecturi="https://9c7a-2409-4066-2-d519-e429-5651-45d1-b00e.ngrok.io/redirect_to_code"
                headers = {'Content-Type': 'application/x-www-form-urlencoded', 'User-Agent': 'OAuth gem v0.4.4'}
                client_id=app.config['CLIENT_ID']
                redirect_uri = redirecturi
                now = datetime.now()
                starts_at=now
                validity=starts_at + relativedelta(months=+2)
                dateCreated=now
                client_secret=app.config['CLIENT_SECRET']
                PARAM = {'grant_type': 'authorization_code',
                'code': AUTH_CODE,
                'redirect_uri': redirect_uri,
                'client_id': client_id,
                'client_secret': client_secret}
                response = requests.post(ACCESS_TOKEN_URL, data=PARAM, headers=headers, timeout=600)
                data = response.json()
                access_token = data['access_token']
                # results=user_service.create_token(app.config['CLIENT_ID'],access_token,validity,dateCreated)
                result=user_service.create_user(clientID=app.config['CLIENT_ID'],accessToken=access_token,validityDate=validity,dateCreated=dateCreated)
                return {"Message":"The Token Generation part has been done."}
            else:
                pass
        except:
            return{"Message":"Either Code Value is Incorrect or Shop Name is Wrong","status":0},400

    def create_user(self,clientID,accessToken,validityDate,dateCreated):
        create_user = linkedintokens_dao.create_new_user(clientID,accessToken,validityDate,dateCreated)
        return {"status":create_user}

    def updating_existing_token(self,URL,redirecturi,scope):
        try:
            client_id=app.config['CLIENT_ID']
            result = user_service.list_all_tokens(client_id)
            token_length=user_service.list_users_by_length(client_id)
            statu=result['users']
            val=0
            for i in statu:
                val=i['validityDate']
            valid_date=val
            current_date=datetime.date.today()
            print("Yes In Updating Token Part")
            if valid_date<=current_date:
                result=user_service.create_auth_link(URL,redirecturi,scope)
                return result
            else:
                print("Herer in no where")
                pass
        except:
            return{"Message":"Kindly give the Correct Code Value if updating the existing Access Token","status":0},400
    

    def add_plans(self,cat_id,name,icon,cost,caption,dateCreated,plan_data):
        create_plans = linkedintokens_dao.add_tokens(cat_id,name,icon,cost,caption,dateCreated,plan_data)
        return {"status":create_plans}

    def get_posts_data(self):
        r1=user_service.list_all_tokens(clientID=app.config['CLIENT_ID'])
        r1_data=r1['users']
        for i in r1_data:
            token=i['accessToken']
        access_token=token
        URL = "https://api.linkedin.com/v2/me"
        headers = {'Content-Type': 'application/x-www-form-urlencoded','Authorization':'Bearer {}'.format(access_token),'X-Restli-Protocol-Version':'2.0.0'}
        response = requests.get(url=URL, headers=headers)
        return response.json()

    def list_all_tokens(self,clientID):
        token=linkedintokens_dao.list_all_tokens(clientID)
        result = linkedintokens_schema.dump(token)
        return ({'users':result})

    def get_plan_detail(self):
        all_users = linkedintokens_dao.get_plan_detail()
        result = linkedintokens_schema.dump(all_users)
        return ({'users':result})

    def list_users_by_length(self,clientID):
        token=linkedintokens_dao.list_users_byclientid(clientID)
        result = linkedintokens_schema.dump(token)
        length_result=len(result)
        return length_result
    
    def list_users_by_length_withoutcid(self):
        token=linkedintokens_dao.list_users_byclientid(app.config['CLIENT_ID'])
        result = linkedintokens_schema.dump(token)
        length_result=len(result)
        return length_result

    def create_auth_link(self,URL,redirecturi,scope):
        client_id=app.config['CLIENT_ID']
        PARAMS = {'response_type':'code', 'client_id':client_id,  'redirect_uri':redirecturi, 'scope':scope}
        r = requests.get(url = URL, params = PARAMS)
        return_url = r.url
        print('Please copy the URL and paste it in browser for getting authentication code')
        return jsonify(return_url)

user_service = UserService()