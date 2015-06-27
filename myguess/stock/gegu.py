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
            print(fileName)
    def guessNext(self):
        return "Gegu test"


if __name__ == '__main__':
    a = Gegu()
    b = Gegu("123456")
    c = Gegu(123)
    b._df = "abc"
    print(b._df)
