#coding=utf-8
from flask import Flask
from stock.view import stock_page
from browse.view import browse_page

app = Flask(__name__)
# 使用Blueprint，url_prefix表示访问路径 #
app.register_blueprint(stock_page, url_prefix='/stock')
app.register_blueprint(browse_page, url_prefix='/browse')

@app.route('/')
def hello_world():
    return 'Hello World!'
