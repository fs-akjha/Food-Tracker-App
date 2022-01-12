from os import access
from flask import Blueprint,request,jsonify,redirect,url_for,Response,session,make_response
import time
from datetime import datetime
import datetime
from flask_cors import cross_origin
from flask_cors import CORS
from flask_ngrok import run_with_ngrok
import requests
import io
from datetime import date
import json
from users.service import user_service
from fsconnectapp.main import main
import hashlib
import tweepy
from tweepy import OAuthHandler
import json
from werkzeug.security import generate_password_hash,check_password_hash


CORS(main)

access_token='159322919-5G9OzdGcSFYV0NJIDsoYR5rQyZRqrApoVAeKKmAv'
access_token_secret='jtmH2khGD4LfXJhOB4tH4bGcn33CakmwgPdDyRhoTfv6V'
consumer_key='YTC8eA09AENEgvCf7lFdHcXha'
consumer_secret='4K1EJlU8NPyAUL1NTO6ZzEzxLG4oTTIA9hSahuN3tvbKP2dZPU'
CLIENT_ID='86v7rsgdm7g3lx'
CLIENT_SECRET='fbjsrylUhOic7bSz'

auth=OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api=tweepy.API(auth)
api = tweepy.API(auth,wait_on_rate_limit = True)

@main.route('/get_auth_link',methods=['GET'])
def get_auth_link():
    URL = "https://www.linkedin.com/oauth/v2/authorization"
    redirecturi="http://127.0.0.1:5000/redirect_to_code"
    client_id=CLIENT_ID
    redirect_uri = redirecturi
    scope='r_organization_social'
    PARAMS = {'response_type':'code', 'client_id':client_id,  'redirect_uri':redirect_uri, 'scope':scope}
    r = requests.get(url = URL, params = PARAMS)
    return_url = r.url
    print('Please copy the URL and paste it in browser for getting authentication code')
    return jsonify(return_url)

@main.route('/redirect_to_code',methods=['GET','POST'])
def redirect_code():
    args=request.args
    Auth_code=args['code']
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'User-Agent': 'OAuth gem v0.4.4'}
    AUTH_CODE = Auth_code
    ACCESS_TOKEN_URL = 'https://www.linkedin.com/oauth/v2/accessToken'
    redirecturi="http://127.0.0.1:5000/redirect_to_code"
    client_id=CLIENT_ID
    redirect_uri = redirecturi
    client_secret=CLIENT_SECRET
    PARAM = {'grant_type': 'authorization_code',
      'code': AUTH_CODE,
      'redirect_uri': redirect_uri,
      'client_id': client_id,
      'client_secret': client_secret}
    response = requests.post(ACCESS_TOKEN_URL, data=PARAM, headers=headers, timeout=600)
    data = response.json()
    access_token = data['access_token']
    URL = "https://api.linkedin.com/v2/posts"
    headers = {'Content-Type': 'application/x-www-form-urlencoded','Authorization':'Bearer {}'.format(access_token),'X-Restli-Protocol-Version':'2.0.0'}
    response = requests.get(url=URL, headers=headers)
    print(response.json())
    get_twitter_data(access_token)
    return response.json()

@main.route('/twitter_data',methods=['GET'])
def get_twitter_data(access_token):
    username="FleetStudio"
    users='fleetstudio'
    print("in Twitter:- ",access_token)
    all_data=[]
    tweets = api.user_timeline(screen_name=username,count=11,tweet_mode = 'extended')
    for tweet in tweets:
        text_data=tweet.full_text
        created_at = tweet.created_at
        source = tweet.source
        ID = tweet.id_str
        user_id=str(tweet.user.id)
        profile_image_url=tweet.user.profile_image_url
        profile_image_url_https=tweet.user.profile_image_url_https
        entities=str(tweet.entities['urls'])
        user_name=tweet.user.name
        user_url=tweet.user.url
        data={
            "Id":ID,
            "user_id":user_id,
            "Post":text_data,
            "Created_at":created_at,
            "Source":source,
            "default_profile":profile_image_url,
            "profile_image_url_https":profile_image_url_https,
            "entities":entities,
            "user_name":user_name,
            "user_url":user_url,
            "platform":"Twitter"
        }
        all_data.append(data)
    return jsonify(all_data)