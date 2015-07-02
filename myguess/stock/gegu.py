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

    def riseDates(self):
        #采集收盘比开盘高的数据
        self.riseDf = self._df[self._df[u'收盘']>self._df[u'开盘']]
        print(self.riseDf)

    def todayRise(self):
        #使用apply，计算收盘减去开盘，需要指定axis=1
        #参考：http://stackoverflow.com/questions/13331698/how-to-apply-a-function-to-two-columns-of-pandas-dataframe
        self._df[u'K值'] = self._df.apply(lambda row: (row[u'收盘']-row[u'开盘']), axis=1)

    def guessNext(self):
        return "Gegu test"


if __name__ == '__main__':
    fileName = "600100.txt"
    mygp = Gegu(fileName)
    #print(mygp._df)
    #print(mygp._df[u'时间'])
    mygp.todayRise()
    print(mygp._df[[u'开盘', u'收盘',u'K值']])
