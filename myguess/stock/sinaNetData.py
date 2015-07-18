#coding=utf-8
import urllib2
import urllib
import httplib

def get_date_sina(date, symbol):
    """
    使用新浪财经进口获取一天的交易数据
    :param date: 日期
    :param symbol: 股票代码
    :return: 一天的交易数据
    """
    url = "http://market.finance.sina.com.cn/downxls.php?"
    params = urllib.urlencode({'date':date, 'symbol':'sh'+symbol})
    data = urllib2.urlopen("%s%s" % (url, params)).read()
    return data

def get_date_sina_2file(date, symbol):
    """
    从新浪财经获取交易信息并保存到文件
    :param date: 日期
    :param symbol: 股票代码
    """
    url = "market.finance.sina.com.cn"
    params = urllib.urlencode({'date':date, 'symbol':'sh'+symbol})
    conn = httplib.HTTPConnection(url)
    print(params)
    conn.request("GET", "/downxls.php?"+params)
    r = conn.getresponse()
    #print(r.getheaders())
    line = r.getheader('content-disposition')
    filename = line[line.index("filename=")+len("filename=\""):-1]
    print(filename)
    with open(filename, 'w') as fo:
        fo.write(r.read())


if __name__ == "__main__":
    get_date_sina("2015-07-16", "600100")
    #get_date_sina_2file("2015-07-16", "600100")

