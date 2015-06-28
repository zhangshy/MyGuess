#coding=utf-8
'''
使用pandas进行个股分析
'''
import pandas as pd
import numpy as np

class Gegu():
    def __init__(self, fileName=None):
        self._df = None
        if isinstance(fileName, str):
            #使用gbk编码方式，delim_whitespace=True使用空格或tab作为分割符
            self._df = pd.read_csv(fileName, encoding="gbk", delim_whitespace=True)
    def guessNext(self):
        return "Gegu test"


if __name__ == '__main__':
    fileName = "600100.txt"
    mygp = Gegu(fileName)
    print(mygp._df)
    #print(mygp._df[u'时间'])
