from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('mysql+pymysql://root:root@localhost/fs_connect', pool_size = 100, pool_recycle=7200)
Session = sessionmaker(bind=engine,expire_on_commit=False)

Base = declarative_base()