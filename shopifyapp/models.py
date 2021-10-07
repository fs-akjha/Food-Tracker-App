from .extensions import db
import pymysql
import datetime
from .extensions import db
from sqlalchemy import Column, Enum, Float, ForeignKey, ForeignKeyConstraint, Index, LargeBinary, String, TIMESTAMP, Table, Text, text, DateTime, func
from sqlalchemy.dialects.mysql import BIGINT, INTEGER, SMALLINT, TINYBLOB, TINYTEXT, TINYINT
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, DateTime




class Masterdb(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    shopURL = db.Column(db.String(150), unique=True, nullable=False)
    firstName = db.Column(db.String(150),nullable=False)
    lastName = db.Column(db.String(150),nullable=False)
    adminEmail = db.Column(db.String(150),nullable=False, unique=True)
    adminPhone=db.Column(db.String(12), unique=True, nullable=False)
    paymentEnableStatus=db.Column(db.Integer)
    subscriptionMode=db.Column(db.Integer)
    subscriptionPlanID=db.Column(db.Integer,unique=True)
    validityDate=db.Column(DateTime, default=datetime.datetime.utcnow)
    status = db.Column(Enum('T', 'F'), nullable=False, server_default=text("'T'"))
    shopName= db.Column(db.String(150), unique=True, nullable=False)
    dateCreated= db.Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))


class Tokens(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    clientID=Column(ForeignKey('masterdb.id'), index=True)
    shopURL = db.Column(db.String(150), unique=True, nullable=False)
    accessToken = Column(String(255), nullable=False)
    validity=db.Column(DateTime, default=datetime.datetime.utcnow)


class Reward_Points(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    customerID=db.Column(db.Integer)
    customerEmail=db.Column(db.String(150),nullable=False, unique=True)
    orderNo=db.Column(db.Integer)
    orderValue=db.Column(db.Integer)
    campaignID=db.Column(db.Integer)
    pointsRewarded=db.Column(db.Integer)
    status=db.Column(Enum('T', 'F'), nullable=False, server_default=text("'T'"))
    dateCreated=db.Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))


class Total_Points(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    customerID=db.Column(db.Integer)
    customerEmail=db.Column(db.String(150),nullable=False, unique=True)
    totalPointsEarned=db.Column(db.Integer)
    totalPointsRedeemed=db.Column(db.Integer)
    totalPoints=db.Column(db.Integer)
    dateUpdated=db.Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))


class Redeem_History(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    customerID=db.Column(db.Integer)
    customerEmail=db.Column(db.String(150),nullable=False, unique=True)
    orderNo=db.Column(db.Integer)
    orderValue=db.Column(db.Integer)
    campaignID=db.Column(db.Integer)
    pointsUsed=db.Column(db.Integer)
    equivalentValue=db.Column(db.Integer)
    status=db.Column(Enum('T', 'F'), nullable=False, server_default=text("'T'"))
    dateCreated=db.Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))