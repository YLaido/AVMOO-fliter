import requests
import string
import httplib2
from bs4 import BeautifulSoup,SoupStrainer
import socket
import socks

#设好各项参数
num   = list(map(str, range(1,30)))
url   = ['https://avmo.pw/cn/star/2ny/page/{}'.format(str(i)) for i in num]  #女优url
#url = 'https://avmo.pw/cn/star/2ny/page/1'
headers   = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'}
list1 = []    #Only For get_link()
中出 = '中出'  #optional
#是否proxy
proxy = {
    'http': 'socks5://127.0.0.1:1080'
}
page = requests.Session()  #which improve the speed
#女优页面,爬取1到29页
def get_page(self):
        wb_data = page.get(self,headers = headers)
        soup1 = BeautifulSoup(wb_data.content, 'lxml')
        select1 = soup1.find_all('a', class_='movie-box')    #找到单个page内所有href
        for link in select1:
            if 中出 in str(link):
                soup2 = BeautifulSoup(str(link), 'lxml')
                print(soup2.get_text())                 #先打印出每个页码中的所有包含关键词'中出'的标题
            else :
                    list1.append(link['href'])
        return list1
#筛选分类函数
def fliter(self):
    url_after2 = page.get(self,headers = headers)
    soup3 = BeautifulSoup(url_after2.content, 'lxml')
    select2 = soup3.select('body > div.container > div.row.movie > div.col-md-3.info > p:nth-of-type(9)') #注意：分类的selector经常变动，即nth-of-type经常变
    str1 = ''.join(str(e) for e in select2) #将select2由list转为string
    soup1 = BeautifulSoup(str1, 'lxml')
    if 中出 in str1:   #按需修改部分参数
        print(soup3.title)
    else:
        pass
#The Main Function
def combine():
    for single in url:
        get_page(single)
    for single2 in list1:
        fliter(single2)

combine()
'''for one in url:
    get_page(one)
print(len(list1))'''
