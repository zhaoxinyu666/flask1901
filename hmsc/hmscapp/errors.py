from hmscapp import app
from flask import render_template
# 错误处理函数
@app.errorhandler(404)
def page_not_found(e):
    # user = User.query.first()
    return render_template('404.html')