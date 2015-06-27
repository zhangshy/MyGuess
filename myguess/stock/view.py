#coding=utf-8
from flask import Blueprint
from gegu import Gegu

stock_page = Blueprint('stock_page', __name__, template_folder='templtes')

@stock_page.route('/')
def index():
    gp = Gegu()
    return gp.guessNext()
