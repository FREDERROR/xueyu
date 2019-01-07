from bs4 import BeautifulSoup
from urllib import request,response
import zlib
import random
import re

base_url = "https://www.bilibili.com"
his = ["/video/av40036315"]
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "}

url = base_url + his[-1]
req = request.Request(url, headers=headers)
res = request.urlopen(req)
html = res.read()
html = zlib.decompress(html, 16 + zlib.MAX_WBITS)  # 解压网页
html_doc = html.decode('utf-8')
soup = BeautifulSoup(html_doc,"html.parser")
userTag = soup.find_all("a",attrs={"class":"name"})
name = userTag[0].get_text()

if name=="雪鱼探店":
    title_list=soup.find_all("h1")
    for title in title_list:
        print(title.attrs["title"]+" "+url)

pattern = re.compile("(/video/av?.*)")
sub_urls = soup.find_all('a',{"href":pattern})
print(sub_urls)
