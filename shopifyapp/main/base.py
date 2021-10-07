from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('mysql+pymysql://root:root@localhost/master_shopify')
Session = sessionmaker(bind=engine,expire_on_commit=False)

Base = declarative_base()