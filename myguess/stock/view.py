#coding=utf-8
from flask import Blueprint, render_template
from gegu import Gegu

stock_page = Blueprint('stock_page', __name__, template_folder='templates')

@stock_page.route('/')
def index():
    return render_template('stock_index.html')
