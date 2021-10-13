from flask import Blueprint,request,session,abort
import time
from datetime import datetime
import datetime
import requests
from users.service import user_service
from shopifyapp.main import main
import base64
import hmac
import hashlib
from utils.service import utils
from Dispatcher.service import dispatcher_data

SECRET='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'
CLIENT_ID='96c349114caa7250b5a40d534ce0bf27'
CLIENT_SECRET='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'

KEY='221434343320303032302302300'

def verify_webhook(data, hmac_header):    
    print(CLIENT_ID)
    digest = hmac.new(SECRET.encode('utf-8'), data, hashlib.sha256).digest()
    genHmac = base64.b64encode(digest)

    return hmac.compare_digest(genHmac, hmac_header.encode('utf-8'))


@main.route('/productCreation', methods=['POST'])
def hello_world():
    print('Received Webhook...')

    data = request.data # NOT request.get_data() !!!!!
    hmac_header = request.headers.get('X-SHOPIFY_HMAC_SHA256')
    verified = verify_webhook(data, hmac_header)
    
    if not verified:
        return 'Integrity of request compromised...', 401
    
    print('Verified request...')





@main.route('/createuser',methods=['GET','POST'])
def create_new_user():
    ts = time.time()
    if request.method == "POST":
            shopURL=request.json['shopURL']
            firstName=request.json['firstName']
            lastName=request.json['lastName']
            adminEmail=request.json['adminEmail']
            adminPhone=request.json['adminPhone']
            paymentEnableStatus=request.json['paymentEnableStatus']
            subscriptionMode=request.json['subscriptionMode']
            subscriptionPlanID=request.json['subscriptionPlanID']
            validityDate=datetime.datetime.utcnow()
            dateCreated=datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
            status=request.json['status']
            shopName=request.json['shopName']
            result=user_service.create_user(shopURL,firstName,lastName,adminEmail,adminPhone,paymentEnableStatus,subscriptionMode,subscriptionPlanID,validityDate,dateCreated,status,shopName)
            return result,200
    else:
        return ({"message":'Kindly do a POST Request'})


@main.route('/getallusers', methods=['GET'])
def get_all_users():
    result = user_service.list_users()
    return result,200


@main.route('/add_tokens',methods=['POST'])
def add_tokens():
    ts = time.time()
    if request.method == "POST":
            params = {
                "client_id":'{}'.format(CLIENT_ID),
                "client_secret":'{}'.format(CLIENT_SECRET),
                "code": '14dc0dfdbe7cf76df6724b3d761a3839'
            }
            shop="fs-rewards-app.myshopify.com"
            resp = requests.post("https://{}/admin/oauth/access_token".format(shop),data=params)
            result=resp.json()
            print(result["access_token"])
            access_token_value=result["access_token"]
            print(resp.json())
            clientID=request.json['clientID']
            shopURL=request.json['shopURL']
            accessToken=access_token_value
            shopName=request.json['shopName']
            validity=request.json['validity']
            result=user_service.create_token(clientID,shopURL,accessToken,shopName,validity)
            return result,200
    else:
        return ({"message":'Its a Post Request'})


@main.route('/add_reward_points',methods=['POST'])
def add_reward_points():
    ts = time.time()
    if request.method == "POST":
            customerID=request.json['customerID']
            customerEmail=request.json['customerEmail']
            orderNo=request.json['orderNo']
            shopName=request.json['shopName']
            orderValue=request.json['orderValue']
            campaignID=request.json['campaignID']
            pointsRewarded=request.json['pointsRewarded']
            status=request.json['status']
            dateCreated=datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
            result=user_service.create_reward_points(customerID,customerEmail,orderNo,orderValue,campaignID,pointsRewarded,status,dateCreated,shopName)
            return result,200
    else:
        return ({"message":'Its a Post Request'})


@main.route('/gett_tokens', methods=['GET','POST'])
def get_all_tokens():
    shopName=request.json['shopName']
    result = user_service.list_all_tokens(shopName)
    return result,200


@main.route('/get_token_byid/<clientID>', methods=['GET','POST'])
def gettokens_byid(clientID):
    shopName=request.json['shopName']
    result = user_service.list_tokens_byid(shopName,clientID)
    return result,200



@main.route('/get_reward_points', methods=['GET','POST'])
def get_all_reward_points():
    shopName=request.json['shopName']
    result = user_service.list_all_rward_points(shopName)
    return result,200


@main.route('/get_reward_points_byid/<customerID>', methods=['GET','POST'])
def getrewardpoints_byid(customerID):
    shopName=request.json['shopName']
    result = user_service.list_rewardpoints_byid(shopName,customerID)
    return result,200

@main.route('/get_reward_points_bymail', methods=['GET','POST'])
def getrewardpoints_bymail():
    shopName=request.json['shopName']
    customerEmail=request.json['customerEmail']
    result = user_service.list_rewardpoints_bymail(shopName,customerEmail)
    return result,200




@main.route('/add_total_points',methods=['POST'])
def add_total_points():
    ts = time.time()
    if request.method == "POST":
            customerID=request.json['customerID']
            customerEmail=request.json['customerEmail']
            totalPointsEarned=request.json['totalPointsEarned']
            totalPointsRedeemed=request.json['totalPointsRedeemed']
            totalPoints=request.json['totalPoints']
            shopName=request.json['shopName']
            dateUpdated=datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
            result=user_service.create_total_points(customerID,customerEmail,totalPointsEarned,totalPointsRedeemed,totalPoints,dateUpdated,shopName)
            return result,200
    else:
        return ({"message":'Its a Post Request'})


@main.route('/get_total_points', methods=['GET','POST'])
def get_all_total_points():
    shopName=request.json['shopName']
    result = user_service.list_total_rward_points(shopName)
    return result,200


@main.route('/get_total_points_byid/<customerID>', methods=['GET','POST'])
def gettotalpoints_byid(customerID):
    shopName=request.json['shopName']
    result = user_service.list_totalpoints_byid(shopName,customerID)
    return result,200

@main.route('/get_total_points_bymail', methods=['GET','POST'])
def gettotalpoints_bymail():
    shopName=request.json['shopName']
    customerEmail=request.json['customerEmail']
    result = user_service.list_totalpoints_bymail(shopName,customerEmail)
    return result,200




@main.route('/redeem_history_points',methods=['POST'])
def redeem_history_points():
    ts = time.time()
    if request.method == "POST":
            customerID=request.json['customerID']
            customerEmail=request.json['customerEmail']
            orderNo=request.json['orderNo']
            orderValue=request.json['orderValue']
            campaignID=request.json['campaignID']
            pointsUsed=request.json['pointsUsed']
            equivalentValue=request.json['equivalentValue']
            status=request.json['status']
            shopName=request.json['shopName']
            dateCreated=datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
            result=user_service.create_redeem_history_points(customerID,customerEmail,orderNo,orderValue,campaignID,pointsUsed,equivalentValue,status,shopName,dateCreated)
            return result,200
    else:
        return ({"message":'Its a Post Request'})

@main.route('/get_redeem_history_data', methods=['GET','POST'])
def get_redeem_history_data():
    shopName=request.json['shopName']
    result = user_service.list_total_redeem_history_data(shopName)
    return result,200


@main.route('/get_redeem_history_data/<customerID>', methods=['GET','POST'])
def getredeemhistorydata_byid(customerID):
    shopName=request.json['shopName']
    result = user_service.list_redeemhistory_data_byid(shopName,customerID)
    return result,200

@main.route('/get_redeem_history_data_bymail', methods=['GET','POST'])
def getredeemhistorydata_bymail():
    shopName=request.json['shopName']
    customerEmail=request.json['customerEmail']
    result = user_service.list_redeemhistory_data_bymail(shopName,customerEmail)
    return result,200








@main.route('/connect', methods=['GET'])
def connect():
    params = {
        "client_id":'96c349114caa7250b5a40d534ce0bf27',
        "client_secret":'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',
        "code": '96e2f5f35684ab70046eabd919253b8d'
    }
    shop="fs-rewards-app.myshopify.com"
    resp = requests.post(
        "https://{}/admin/oauth/access_token".format(shop),
        data=params
    )
    result=resp.json()
    print(result["access_token"])
    print(resp.json())
    return resp.json()
