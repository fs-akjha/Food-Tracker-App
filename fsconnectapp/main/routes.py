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
from fsconnectapp.main import app
from werkzeug.security import generate_password_hash,check_password_hash
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import urllib.request
from bs4 import BeautifulSoup



CORS(main)

access_token=app.config['ACCESS_TOKEN']
access_token_secret=app.config['ACCESS_TOKEN_SECRET']
consumer_key=app.config['CONSUMER_KEY']
consumer_secret=app.config['CONSUMER_SECRET']

auth=OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api=tweepy.API(auth)
api = tweepy.API(auth,wait_on_rate_limit = True)

# @main.route('/get_auth_link',methods=['GET'])
# @cross_origin()
# def get_auth_link():
#     URL = "https://www.linkedin.com/oauth/v2/authorization"
#     redirecturi="http://127.0.0.1:5000/redirect_to_code"
#     client_id=CLIENT_ID
#     redirect_uri = redirecturi
#     scope='r_organization_social'
#     PARAMS = {'response_type':'code', 'client_id':client_id,  'redirect_uri':redirect_uri, 'scope':scope}
#     r = requests.get(url = URL, params = PARAMS)
#     return_url = r.url
#     print('Please copy the URL and paste it in browser for getting authentication code')
#     return jsonify(return_url)

@main.route('/redirect_to_code',methods=['GET','POST'])
@cross_origin()
def redirect_code():
    args=request.args
    try:
        Auth_code=args['code']
        response=user_service.creating_new_token(Auth_code)
    except:
        print("In Except")
    username="FleetStudio"
    users='fleetstudio'
    all_datas=[]
    link_post=user_service.get_posts_data()
    print(link_post)
    # last_name=link_post['localizedLastName']
    # first_name=link_post['localizedFirstName']
    # # profile_pic=link_post['profilePicture']
    # id=link_post['id']
    # link_data={
    #     "Id":id,
    #     "First_name":first_name,
    #     "Last_name":last_name,
    #     # "Profile_Picture":profile_pic,
    #     "Platform":"Linkedin"
    # }
    # all_datas.append(link_data)
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
        all_datas.append(data)
    siteurl = "https://api.rss2json.com/v1/api.json?rss_url=https://fleetstudio.medium.com/feed"
    page = requests.get(siteurl)
    all_data=page.json()
    med_status=all_data['status']
    med_feeds=all_data['feed']
    med_items=all_data['items']
    for mi in med_items:
        post_title=mi['title']
        pub_date=mi['pubDate']
        post_link=mi['link']
        post_guid=mi['guid']
        author=mi['author']
        thumbnail=mi['thumbnail']
        post_description=mi['description']
        categories=mi['categories']
        mi_data={
            "URL":med_feeds['url'],
            "Title":med_feeds['title'],
            "Link":med_feeds['link'],
            "Description":med_feeds['description'],
            "Image":med_feeds['image'],
            "PostTitle":post_title,
            "PublishedDate":pub_date,
            "PostLink":post_link,
            "PostGUID":post_guid,
            "Author":author,
            "Thumbnail":thumbnail,
            "PostDescription":post_description,
            "Categories":categories,
            "platform":"Medium"
        }
        all_datas.append(mi_data)
    return jsonify(all_datas)

@main.route('/get_medium_data',methods=['GET'])
@cross_origin()
def get_medium_data():
    siteurl = "https://api.rss2json.com/v1/api.json?rss_url=https://fleetstudio.medium.com/feed"
    page = requests.get(siteurl)
    all_data=page.json()
    med_status=all_data['status']
    med_feeds=all_data['feed']
    med_items=all_data['items']
    mf_data={
        "URL":med_feeds['url'],
        "Title":med_feeds['title'],
        "Link":med_feeds['link'],
        "Description":med_feeds['description'],
        "Image":med_feeds['image']
    }
    for mi in med_items:
        post_title=mi['title']
        pub_date=mi['pubDate']
        post_link=mi['link']
        post_guid=mi['guid']
        author=mi['author']
        thumbnail=mi['thumbnail']
        post_description=mi['description']
        categories=mi['categories']
        mi_data={
            "PostTitle":post_title,
            "PublishedDate":pub_date,
            "PostLink":post_link,
            "PostGUID":post_guid,
            "Author":author,
            "Thumbnail":thumbnail,
            "PostDescription":post_description,
            "Categories":categories
        }
    merged_dict={**mf_data,**mi_data}
    return merged_dict

@main.route('/twitter_data',methods=['GET'])
@cross_origin()
def get_twitter_data():
    result_users=user_service.list_users_by_length_withoutcid()
    if(result_users<1):
        URL = "https://www.linkedin.com/oauth/v2/authorization"
        redirecturi="https://6a71-2409-4066-103-5d5d-bd3c-f13e-73b8-9761.ngrok.io/redirect_to_code"
        scope='r_organization_social'
        result=user_service.create_auth_link(URL,redirecturi,scope)
        return result
    else:
        URL = "https://www.linkedin.com/oauth/v2/authorization"
        redirecturi="https://6a71-2409-4066-103-5d5d-bd3c-f13e-73b8-9761.ngrok.io/redirect_to_code"
        scope='r_organization_social'
        user_service.updating_existing_token(URL,redirecturi,scope)
        return redirect('https://6a71-2409-4066-103-5d5d-bd3c-f13e-73b8-9761.ngrok.io/redirect_to_code')