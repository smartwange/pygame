import requests
from bs4 import BeautifulSoup as bs
from time import sleep
# 直接请求返回418，拒接爬取数据，解决办法，伪装成浏览器。
# 有些网站通过ip限制一定时间内可访问次数，需要动态切换ip和user_agent
def getPageData(url):
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'
    header = {}
    header['user-agent'] = user_agent
    response = requests.get(url, headers=header)
    # print(response.text)
    bs_info = bs(response.text, 'html.parser')
    # bs第二个参数是分析器方式 html/lxml/xml
    for tags in bs_info.find_all('div', attrs={'class': 'pl2'}):
        for atag in tags.find_all('a'):
            print(atag.get('href'))
            print(atag.get('title'))
# print(list1)
# 3.6以上可以使用f-string，类似format
urls=tuple(f'https://book.douban.com/top250?start={page*25}' for page in range(10))
# 给代码调用做个入口
if __name__ == '__main__':
    for page in urls:
        getPageData(page)
        # 请求过快，爬取内容是空的,也是反爬虫的限制
        sleep(5)