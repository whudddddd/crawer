import urllib
import urllib.request
import re
import urllib.error

proxy = {'http': '122.114.31.177'}
proxy_support = urllib.request.ProxyHandler(proxy)
opener = urllib.request.build_opener(proxy_support)
url="https://www.xicidaili.com/nn/"
user_agent="Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0)"
header={'user-agent',user_agent}
opener.add_handler=[header]
urllib.request.install_opener(opener)
try:
    reponse=urllib.request.urlopen(url)
    content=reponse.read().decode('utf-8')
    #pattern=re.compile(r"<td classs.*?</td><td>(.*?)</td>")
    #items=re.findall(pattern,content)
    print(content)
except urllib.error.URLError as e:
    if hasattr(e,'code'):
        print(e.code)
    if hasattr(e,'reason'):
        print(e.reason)