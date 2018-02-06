import urllib.request
import re
a='scra caSc da dSd adsc sc  ada dada'
b=re.findall(r's.*?c',a)
print(b)