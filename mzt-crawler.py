import urllib.request
import urllib
import urllib.error
import re
import time

url='http://www.meizitu.com/'
user_agent="Mozilla/5.0 (Windows NT 10.0; Win64;x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Safari/537.36 Edge/16.16299)"
headers = {'user-agent',user_agent}
opener=urllib.request.build_opener()
opener.addheaders=[headers]
urllib.request.install_opener(opener)
try:
    response=urllib.request.urlopen(url)
    content = response.read().decode('gbk')
    pattern = re.compile(r'<img src="(.+?)" alt=".+?"></a></li>')
    items = re.findall(pattern,content )
    #urllib.request.urlretrieve(items[1], '1.jpg')
    x=0
    for item in items:
        urllib.request.urlretrieve(item, '%s.jpg' % x)
        x += 1
        time.sleep(2)
except urllib.error.URLError as e:
    if hasattr(e,'code'):
        print(e.code)
    if hasattr(e,'reason'):
        print(e.reason)