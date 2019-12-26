# 獲得專輯照片&其他排名的歌名資料
# 把下面的code插入在16行那邊
# 目前我只做華語歌曲前十名的專輯照片網址

man_url = url + song_list[0]
r_man = requests.get(man_url)
soup = BeautifulSoup(r_man.text, 'html.parser')
all_scripts = soup.find_all('script')
song_scripts = all_scripts[-2].text[:-30000] # 後面一大段都不重要


man_cover = []  # 前十名的專輯照片網址

for i in range(10):

    #處理專輯照片
    start = song_scripts.find('small')
    end = song_scripts.find('160x160.jpg')
    cover_url = song_scripts[start+8:end+11]
    cover_url = cover_url.replace('\\' , '')
    man_cover.append(cover_url)

    # 把文字檔精簡
    song_scripts = song_scripts[end+12:]