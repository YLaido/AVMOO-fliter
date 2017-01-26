import requests
from bs4 import BeautifulSoup,SoupStrainer
import traceback

# 设好各项参数
num = list(map(str, range(1,30)))
url = ['https://avmo.pw/cn/search/123/page/{}'.format(str(i)) for i in num]  #女优url
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'}
list1 = []    #Only For get_link()
key_word = '肛'  #optional
proxy = {
    'http': 'socks5://127.0.0.1:1082'
}
page = requests.Session()
# 女优页面,爬取1到29页
def get_page(self):
    try:
        wb_data = page.get(self,headers = headers)
        soup1 = BeautifulSoup(wb_data.content, 'lxml',parse_only=SoupStrainer('a',{'class': 'movie-box'}))
        for link in soup1.contents[1:]:
            if key_word in link.span.get_text():
                print(link.span.get_text() + '  ' +link['href']) 
            else:
                list1.append(link['href'])
        return list1
    except:
        traceback.print_exc()
        pass
# 筛选分类函数
def fliter(self):
    r = page.get(self,headers = headers)
    soup2 = BeautifulSoup(r.content, 'lxml',parse_only=SoupStrainer('span',{'class': 'genre'}))
    for g in soup2.contents[1:]:
        if key_word in g.get_text():
            soup3 = BeautifulSoup(r.content, 'lxml',parse_only=SoupStrainer('h3'))
            print(soup3.contents[1].get_text() + '   ' + r.url)
        else:
            pass

#The Main Function
def combine():
    for single in url:
        get_page(single)
    for single2 in list1:
        fliter(single2)


combine()
