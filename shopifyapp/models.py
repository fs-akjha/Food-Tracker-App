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