import urllib.request
import urllib
import urllib.error
import re

page=1
for page in range(1,3):
    proxy={'http':'122.114.31.177'}
    proxy_support=urllib.request.ProxyHandler(proxy)
    opener=urllib.request.build_opener(proxy_support)
    url="https://www.qiushibaike.com/8hr/page/"+str(page)
    user_agent="Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0)"
    headers = {'user-agent',user_agent}
  #  opener=urllib.request.build_opener()
    opener.addheaders=[headers]
    urllib.request.install_opener(opener)
    try:
        response=urllib.request.urlopen(url)
        content = response.read().decode('utf-8')
        print(content)
        #pattern = re.compile('<div.*?"author (.*?)">.*?<a.*?<.*?img>(.*?)</a>.*?<div.*?"content>(.*?)+'
        #                    '<div class="stats"><!--(.*?--)>.*? class="number">(.*?)</i> ')
        pattern = re.compile(r'<div.*?author clearfix">.*?<h2>(.*?)</h2>.*?<div.*?span>(.*?)</span>.*?<!--.*?-->.*?<img src="(.*?)" alt=.*?>.*?</i>',re.S)
        items = re.findall(pattern,str(content) )
        for item in items:
             haveimg = re.search("img", item[2])
             if not haveimg:
                 print(item[0], item[1])
    except urllib.error.URLError as e:
        if hasattr(e,'code'):
            print(e.code)
        if hasattr(e,'reason'):
            print(e.reason)

