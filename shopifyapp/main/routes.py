from flask import Blueprint, render_template, request, redirect, url_for,session
import time
from datetime import datetime
import datetime
import requests
from users.service import user_service
from shopifyapp.main import main
import json
import shopify



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
            clientID=request.json['clientID']
            shopURL=request.json['shopURL']
            accessToken=request.json['accessToken']
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
        "code": 'cd0d65a3ed5d0c21d8c40c5f3411ccb9'
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
    