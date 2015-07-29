#coding=utf-8
from flask import Blueprint, render_template
import browseDir

browse_page = Blueprint('browse_page', __name__, template_folder='templates')

@browse_page.route('/')
def index():
    mp3s = browseDir.getAllMp3s()
    #使用sorted对list进行排序
    return render_template('browse_index.html', files = sorted(mp3s.items()))

