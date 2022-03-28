from .extensions import db
import pymysql
import datetime
from .extensions import db
from sqlalchemy import Column, Enum, Float, ForeignKey, ForeignKeyConstraint, Index, LargeBinary, String, TIMESTAMP, Table, Text, text, DateTime, func
from sqlalchemy.dialects.mysql import BIGINT, INTEGER, SMALLINT, TINYBLOB, TINYTEXT, TINYINT
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, DateTime

class LinkedinTokens(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    clientID = db.Column(db.String(255), unique=False, nullable=False)
    accessToken= db.Column(db.Text,unique=False, nullable=False)
    refresh_accessToken= db.Column(db.Text,unique=False, nullable=True)
    status = db.Column(db.Integer, server_default=text("1"))
    validityDate=db.Column(DateTime, default=datetime.datetime.utcnow)
    refresh_token_validityDate=db.Column(DateTime, default=datetime.datetime.utcnow)
    dateCreated= db.Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))