#coding=utf-8
'''
使用pandas进行个股分析
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

class Gegu():
    def __init__(self, fileName=None):
        self._df = None
        self.completed = False
        if isinstance(fileName, str):
            #使用gbk编码方式，delim_whitespace=True使用空格或tab作为分割符
            self._df = pd.read_csv(fileName, encoding="gbk", delim_whitespace=True)

    def riseDates(self):
        #采集收盘比开盘高的数据
        self.riseDf = self._df[self._df[u'收盘']>self._df[u'开盘']]
        print(self.riseDf)

    def todayRise(self):
        #使用apply方法，计算收盘减去开盘，对行进行操作需要指定axis=1
        #参考：http://stackoverflow.com/questions/13331698/how-to-apply-a-function-to-two-columns-of-pandas-dataframe
        self._df[u'K值'] = self._df.apply(lambda row: (row[u'收盘']-row[u'开盘']), axis=1)

    def completeData(self):
        """
        使用DataFrame.iterrows遍历行，计算当天数据
        """
        row_iterator = self._df.iterrows()
        _, last = row_iterator.next()   #取第一行数据
        for i, row in row_iterator:
            self._df.loc[i, u'K值'] = row[u'收盘'] - row[u'开盘']   #当天的收盘价减开盘价
            self._df.loc[i, u'涨跌'] = row[u'收盘'] - last[u'收盘'] #dataframe.loc修改指定位置数据
            self._df.loc[i, u'高开'] = row[u'开盘'] - last[u'收盘'] #开盘价减昨天收盘价
            last = row
        self.completed = True

    def infos(self):
        self.info = {}
        if not self.completed:
            self.completeData()
        self.info['counts'] = len(self._df.index) #行数
        self.info['k_up'] = len(self._df[self._df[u'K值']>0].index)
        self.info['k_down'] = len(self._df[self._df[u'K值']<0].index)
        self.info['k_equal'] = len(self._df[self._df[u'K值']==0].index)
        self.info['up'] = len(self._df[self._df[u'涨跌']>0].index)
        self.info['down'] = len(self._df[self._df[u'涨跌']<0].index)
        self.info['equal'] = len(self._df[self._df[u'涨跌']==0].index)
        return self.info

    def continue_list(self):
        """
        记录连续上涨或连续下跌的天数
        :return:
        """
        ups = [[] for i in range(15)]
        downs = [[] for i in range(15)]
        if not self.completed:
            self.completeData()
        s = 0
        uping = False
        for i, row in self._df.iterrows():
            if row[u'涨跌']>=0:
                if not uping:
                    if s!=0:
                        downs[s-1].append(i)
                        s = 0
                uping = True
                s += 1
            else:
                if uping:
                    if s!=0:
                        ups[s-1].append(i)
                        s = 0
                uping = False
                s += 1
        ret = {}
        ret["ups"] = ups
        ret['downs'] = downs
        return ret


    def guessNext(self):
        return "Gegu test"


if __name__ == '__main__':
    basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) #os.path.dirname可获取上一级目录
    fileName = os.path.join(basedir, "data", "600100.txt")
    print("fileName:%s" % (fileName))
    mygp = Gegu(fileName)
    #print(mygp._df)
    #print(mygp._df[u'时间'])
    mygp.completeData()
    #print(mygp._df[[u'开盘', u'收盘',u'K值', u'涨跌', u'高开']])
    #mygp._df.iloc[-10:].plot(x=u'时间', y=[u'涨跌', u'高开', u'收盘'])
    #mygp._df.iloc[-10:].plot(x=u'时间', y=[u'涨跌', u'高开', u'收盘']) #DataFrame.iloc[-10:]取后10行数据
    #plt.savefig("test.svg", format="svg")#保存svg格式图片
    #plt.show() #添加plt.show()才能在程序中显示出图表
    info = mygp.infos()
    print(info)
    ret = mygp.continue_list()
    print(ret)
    ups = ret['ups']
    downs = ret['downs']
    print(ups)
    print([len(t) for t in ups])
    print(downs)
    print([len(t) for t in downs])

