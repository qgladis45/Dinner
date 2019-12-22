import requests
from bs4 import BeautifulSoup
import tkinter as tk
import webbrowser

url = 'https://kma.kkbox.com/charts/daily/song?cate='
song_list = ['297', '390', '308', '314', '304', '320'] # 華語man,英文eng,日文jap,韓文kor,台語twn,粵語can
song_index = -1

man_rank = []
eng_rank = []
jap_rank = []
kor_rank = []
twn_rank = []
can_rank = []

for o in (man_rank, eng_rank, jap_rank, kor_rank, twn_rank, can_rank):
    song_index += 1
    song_url = url + song_list[song_index]

    r = requests.get(song_url)

    soup = BeautifulSoup(r.text, 'html.parser')
    attr = {'name': 'description'}

    rank = soup.find_all('meta', attrs = attr)     # 找到html裡面的meta標籤
    rank_str = rank[0]['content']                  # 找到排行榜的部分
    rank_str = rank_str[(rank_str.find('：')+1):]  # 只抓取歌單的部分
    rank_list = rank_str.split('、')               # 把str轉成list


    # list中0,2,4,6,8為歌名; 1,3,5,7,9為歌手
    for i in rank_list:
        #rank = i.strip()
        title = i[:i.find('-')]       # 把歌名整理一下
        singer = i[(i.find('-')+1):]  # 把歌手整理一下
        if title.find('('):           # 如果歌名有(像是歌名的英文名稱)
            o.append(title[:title.find('(')])  # 只保留中文的部分
        else:
            o.append(title)

        if singer.find('-'):
            o.append(singer[(singer.find('-')+1):])
        else:
            o.append(singer)

    # 把前後有空格的整理乾淨
    for i in range(10):
        o[i] = o[i].strip()


'''視窗'''
class Ranking(tk.Frame):

    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.buttons()
        self.click_man()
    
    def buttons(self):
        self.manbut = tk.Button(self, text='華語', command=self.click_man)
        self.manbut.grid(row=0, column=0)
        self.engbut = tk.Button(self, text='西洋', command=self.click_eng)
        self.engbut.grid(row=0, column=1)
        self.japbut = tk.Button(self, text='日語')
        self.japbut.grid(row=0, column=2)
        self.korbut = tk.Button(self, text='韓語')
        self.korbut.grid(row=0, column=3)
        self.twnbut = tk.Button(self, text='台語')
        self.twnbut.grid(row=0, column=4)
        self.canbut = tk.Button(self, text='粵語')
        self.canbut.grid(row=0, column=5)
        
        self.rank1 = tk.Label(self, text='第一名')
        self.rank1.grid(row=1, column=0)
        self.rank2 = tk.Label(self, text='第二名')
        self.rank2.grid(row=2, column=0)
        self.rank3 = tk.Label(self, text='第三名')
        self.rank3.grid(row=3, column=0)
        self.rank4 = tk.Label(self, text='第四名')
        self.rank4.grid(row=4, column=0)
        self.rank5 = tk.Label(self, text='第五名')
        self.rank5.grid(row=5, column=0)

    def click_man(self):
        self.man1 = tk.Button(self, text=(man_rank[0]+man_rank[1]), command=self.click_man1)
        self.man1.grid(row=1, column=1, columnspan=6)
        self.man2 = tk.Button(self, text=(man_rank[2]+man_rank[3]))
        self.man2.grid(row=2, column=1, columnspan=6)
        self.man3 = tk.Button(self, text=(man_rank[4]+man_rank[5]))
        self.man3.grid(row=3, column=1, columnspan=6)
        self.man4 = tk.Button(self, text=(man_rank[6]+man_rank[7]))
        self.man4.grid(row=4, column=1, columnspan=6)
        self.man5 = tk.Button(self, text=(man_rank[8]+man_rank[9]))
        self.man5.grid(row=5, column=1, columnspan=6)
        
    def click_man1(self):
        webbrowser.open_new_tab('https://www.youtube.com/results?search_query=' + str(man_rank[0]) + '+' + str(man_rank[1]))
    
    def click_eng(self):
        self.eng1 = tk.Button(self, text='英語1', command=self.click_eng1)
        self.eng1.grid(row=1, column=1, columnspan=6)
        self.eng2 = tk.Button(self, text='英語2')
        self.eng2.grid(row=2, column=1, columnspan=6)
        self.eng3 = tk.Button(self, text='英語3')
        self.eng3.grid(row=3, column=1, columnspan=6)
        self.eng4 = tk.Button(self, text='英語4')
        self.eng4.grid(row=4, column=1, columnspan=6)
        self.eng5 = tk.Button(self, text='英語5')
        self.eng5.grid(row=5, column=1, columnspan=6)
    
    def click_eng1(self):
        #webbrowser.open_new_tab('https://www.youtube.com/results?search_query=' + str(eng_rank[0]) + '+' + str(eng_rank[1]))
        webbrowser.open_new_tab('https://www.youtube.com')


'''
    def click_jap(self):
        self.man1 = tk.Button(self, text='華語1')
        self.man1.grid(row=1, column=1, columnspan=6)
        self.man2 = tk.Button(self, text='華語2')
        self.man2.grid(row=2, column=1, columnspan=6)
        self.man3 = tk.Button(self, text='華語3')
        self.man3.grid(row=3, column=1, columnspan=6)
        self.man4 = tk.Button(self, text='華語4')
        self.man4.grid(row=4, column=1, columnspan=6)
        self.man5 = tk.Button(self, text='華語5')
        self.man5.grid(row=5, column=1, columnspan=6)

    def click_kor(self):
        self.man1 = tk.Button(self, text='華語1')
        self.man1.grid(row=1, column=1, columnspan=6)
        self.man2 = tk.Button(self, text='華語2')
        self.man2.grid(row=2, column=1, columnspan=6)
        self.man3 = tk.Button(self, text='華語3')
        self.man3.grid(row=3, column=1, columnspan=6)
        self.man4 = tk.Button(self, text='華語4')
        self.man4.grid(row=4, column=1, columnspan=6)
        self.man5 = tk.Button(self, text='華語5')
        self.man5.grid(row=5, column=1, columnspan=6)
'''
ranking = Ranking()
ranking.master.title("KKbox Ranking")
ranking.mainloop()