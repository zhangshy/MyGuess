#coding=utf-8
import os

#mp3Dir = os.path.join("D:", "BaiduYunDownload")
mp3Dir = "D:\\BaiduYunDownload"

def getAllMp3s():
    baseLen = len(mp3Dir)+1
    mp3s = {}
    print(mp3Dir)
    for parent, dirnames, filenames in os.walk(mp3Dir):
        ##使用os.walk遍历目录
        for filename in filenames:
            if filename.endswith('.mp3'):
                #print(filename.decode('gbk')) #window下中文路径使用gbk编码
                #print(os.path.join(parent, filename)[baseLen:].decode('gbk'))
                mp3s[filename] = os.path.join(parent, filename)[baseLen:]
    return mp3s

if __name__ == '__main__':
    files = getAllMp3s()
    for key, value in sorted(files.items()):
        #使用sorted进行排序
        print(value.decode('gbk'))

