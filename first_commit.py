import requests
import string
import httplib2
from bs4 import BeautifulSoup,SoupStrainer

#设好各项参数
num   = list(map(str, range(1,30)))
url   = ['https://avmo.pw/cn/star/2ny/page/{}'.format(str(i)) for i in num]
headers   = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'}
list1 = []  #Only For get_link()
中出 = '中出'
#女优页面,爬取1到29页
def get_page(self):
        wb_data = requests.get(self,headers = headers)
        soup1 = BeautifulSoup(wb_data.content, 'lxml')
      #  selects = soup1.select('#waterfall > div > a > div.photo-info > span')    #抓取页面内所有教育片标题
        select1 = soup1.find_all('a', class_='movie-box')       #找到单个page内所有href
        for link in select1:
                if link.has_attr('href'):
                    list1.append(link['href'])
        #print(list1)                               #女优所有作品href的list

#抓取页面内所有link
'''def get_link(self):
    url_after1 = requests.get(self,headers = headers)
    soup2 = BeautifulSoup(url_after1.content, 'lxml')
    select1 = soup2.find_all('a', class_= 'movie-box')
    for link in select1:
        if link.has_attr('href'):
            list1.append(link['href'])
    print(list1)'''

#筛选分类函数
def fliter(self):
    url_after2 = requests.get(self,headers = headers)
    soup3 = BeautifulSoup(url_after2.content, 'lxml')
    select2 = soup3.select('body > div.container > div.row.movie > div.col-md-3.info > p:nth-of-type(12)')
    str1 = ''.join(str(e) for e in select2) #将select2由list转为string
    soup1 = BeautifulSoup(str1, 'lxml')
    if 中出 in str1:   #按需修改部分参数
        print(soup3.title)
    else:
        pass

for single_url in url:
    get_page(single_url)
for item in list1:
    fliter(item)