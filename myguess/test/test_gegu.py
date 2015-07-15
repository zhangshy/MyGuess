#coding=utf-8

import os
import unittest
import myguess.stock

class gegutest(unittest.TestCase):

    ##初始化工作
    def setUp(self):
        basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) #os.path.dirname可获取上一级目录
        fileName = os.path.join(basedir, "data", "600100.txt")
        print("fileName:%s" % (fileName))
        self.mygp = myguess.stock.gegu.Gegu(fileName)

    ##退出清理工作
    def tearDown(self):
        pass

    ##测试
    def test_infos(self):
        self.assertIsInstance(self.mygp.infos(), dict)

if __name__ == '__main__':
    unittest.main()