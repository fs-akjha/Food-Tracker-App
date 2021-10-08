from flask import Blueprint, render_template, request, redirect, url_for
import time
import datetime
from datetime import datetime
import datetime
from users.service import user_service
from shopifyapp.main import main



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
            dateCreated=datetime.datetime.utcnow()
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