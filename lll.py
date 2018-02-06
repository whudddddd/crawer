
#coding=utf-8
import urllib.request
import re
def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read().decode()
    return html
def getImg(html):
    reg = r'src="(.+?)" '
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    print(html)
    print(imglist)
    x = 0
    '''for imgurl in imglist:
        urllib.request.urlretrieve(imgurl,'%s.jpg' % x)
        x+=1'''
html = getHtml("https://cn.bing.com/images/trending?form=ILPASW")
getImg(html)
