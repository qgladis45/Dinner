import requests
from bs4 import BeautifulSoup

man = 'https://kma.kkbox.com/charts/daily/song?cate=297'
eng = 'https://kma.kkbox.com/charts/daily/song?cate=390'
jap = 'https://kma.kkbox.com/charts/daily/song?cate=308'
kor = 'https://kma.kkbox.com/charts/daily/song?cate=314'
twn = 'https://kma.kkbox.com/charts/daily/song?cate=304'
can = 'https://kma.kkbox.com/charts/daily/song?cate=320'


r = requests.get(man)
soup = BeautifulSoup(r.text, 'html.parser')
attr = {'name': 'description'}

rank = soup.find_all('meta', attrs = attr)     # 找到html裡面的meta標籤
rank_str = rank[0]['content']                  # 找到排行榜的部分
rank_str = rank_str[(rank_str.find('：')+1):]  # 只抓取歌單的部分
rank_list = rank_str.split('、')               # 把str轉成list

rank_songtitle = []
rank_singer = []

# print(rank_list)

for i in rank_list:
    #rank = i.strip()
    title = i[:i.find('-')]       # 把歌名整理一下
    singer = i[(i.find('-')+1):]  # 把歌手整理一下
    if title.find('('):           # 如果歌名有(像是歌名的英文名稱)
        rank_songtitle.append(title[:title.find('(')])  # 就只保留中文的部分
    else:
        rank_songtitle.append(title)

    if singer.find('-'):
        rank_singer.append(singer[(singer.find('-')+1):])
    else:
        rank_singer.append(singer)

# 把前後有空格的整理乾淨
for i in range(5):
    rank_singer[i] = rank_singer[i].strip()
    rank_songtitle[i] = rank_songtitle[i].strip()

#for i in range(5):
#    print(rank_singer[i])
#    print(rank_songtitle[i])
#    print('-----------------')