#/usr/bin/env python
#coding:UTF-8
import time
import os,sys
import urllib.request


fileName = '661365'
downdir = '//Users/michaelliu/Downloads/taotu8/'

def downloadFile(url,fileName):
	urllib.request.urlretrieve(url, fileName)


def downloadbag():
    if (not os.path.exists(downdir+fileName)):
        os.mkdir(downdir+fileName)
    os.chdir(downdir+fileName)
    
    for x in range(100):
        temp = fileName+str(x)
        url = 'https://la.killcovid2021.com/m3u8/'+fileName+'/'+temp+'.ts'
        downloadFile(url,temp+'.ts')
        pass

downloadbag()