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