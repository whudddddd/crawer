import urllib
import urllib.request
import re
import urllib.error
import time

url ="http://tieba.baidu.com/p/5501280655"
reponse=urllib.request.urlopen(url)
content=reponse.read().decode()
pattern = re.compile(r'<br><img .+? src="(.+?)" size.+?>')
imglists=re.findall(pattern,content)
x=0
for imglist in imglists:
    haveimg = re.search("png", imglist)
    if not haveimg:
        urllib.request.urlretrieve(imglist,'%s.jpg'%x)
    x=x+1