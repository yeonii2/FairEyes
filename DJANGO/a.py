import requests
from bs4 import BeautifulSoup

page = requests.get('https://qz.com/africa/latest')
soup = BeautifulSoup(page.content, 'html.parser')

weblinks = soup.find_all('article')

# print 명령어를 차례로 지워나가면서 변수 값 확인해 보세요
print(soup)
print(weblinks[0])
print(weblinks[1])
print(weblinks[2])
print(weblinks[3])
print(weblinks[4])

pagelinks = []


for link in weblinks[5:]:
    url = link.contents[0].find_all('a')[0]
    pagelinks.append('http://qz.com'+url.get('href'))

    # 여기서도 print 명령어 번갈아 지워보면서 확인해 보세요
    print(url)
    print(url.get('href'))
    print(pagelinks)