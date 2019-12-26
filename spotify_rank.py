import requests
from bs4 import BeautifulSoup

spotify_url = 'https://spotifycharts.com/regional/tw/daily/latest'

r = requests.get(spotify_url)
soup = BeautifulSoup(r.text, 'html.parser')
attr = {'class': 'chart-table-track'}
rank = soup.find_all('td', attrs = attr)     # 找到html裡面的td標籤

top_num = 0


sp_rank = []

for i in rank:
    song = i.get_text().strip()
    song = song.split('\nby')
    sp_rank.append(song[0])  # 歌名
    sp_rank.append(song[1])  # 歌手


    # 這邊決定要前多少名
    top_num += 1
    if top_num == 20:
        break

# print(sp_rank)