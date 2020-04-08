import os,sys

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


app = Flask(__name__)
WIN = sys.platform.startswith('win')
if WIN:
    prefix = "sqlite:///" # windows平台
else:
    prefix = "sqlite:////" #Mac，Linux平台
app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(os.path.dirname(app.root_path),'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '1903_dev'

db = SQLAlchemy(app)

login_manager = LoginManager(app) # 实例化扩展类
@login_manager.user_loader
def load_user(user_id): # 创建用户加载回调函数，接收用户ID作为参数
    from watchlist.models import User
    user = User.query.get(user_id)
    return user
# 如果操作了需要登录才有的操作，系统会跳转到登录页面
login_manager.login_view = 'login'

# 模板上下文处理函数
@app.context_processor
def common_user():
    from watchlist.models import User
    user = User.query.first()
    return dict(user=user)


from watchlist import views, errors, commands