import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, String, Integer, Float, Date
from sqlalchemy.ext.declarative import declarative_base

# 建立连接与数据库的连接
engine = create_engine('mysql+pymysql://seamile:54188@localhost:3306/homework')
Base = declarative_base(bind=engine)  # 创建模型的基础类
Session = sessionmaker(bind=engine)   # 创建会话类
session = Session()


class User(Base):
    '''类本身对应数据库里的表结构'''
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), unique=True)
    birthday = Column(Date, default=datetime.date(1990, 1, 1))
    city = Column(String(10), default='上海')
    money = Column(Float, default=0.0)
