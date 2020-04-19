# python自带的
import os
import sys

from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_login import LoginManager

app = Flask(__name__)
WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'

# linux下四条杠
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////'+os.path.join(app.root_path,'data.db')
# Windows下三条杠
app.config['SQLALCHEMY_DATABASE_URI'] = prefix+os.path.join(os.path.dirname(app.root_path),'data.db')
# 关闭了对模型修改的监控
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'hmsclist_dev'
# 初始化扩展，传入程序实例app
db = SQLAlchemy(app)



from hmscapp import views,errors