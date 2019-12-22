import requests
from bs4 import BeautifulSoup
import tkinter as tk
import webbrowser

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

'''視窗'''
class Ranking(tk.Frame):

    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.buttons()
    
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
        self.man1 = tk.Button(self, text=(rank_songtitle[0]+rank_singer[0]), command=self.click_man1)
        self.man1.grid(row=1, column=1, columnspan=6)
        self.man2 = tk.Button(self, text=(rank_songtitle[1]+rank_singer[1]))
        self.man2.grid(row=2, column=1, columnspan=6)
        self.man3 = tk.Button(self, text=(rank_songtitle[2]+rank_singer[2]))
        self.man3.grid(row=3, column=1, columnspan=6)
        self.man4 = tk.Button(self, text=(rank_songtitle[3]+rank_singer[3]))
        self.man4.grid(row=4, column=1, columnspan=6)
        self.man5 = tk.Button(self, text=(rank_songtitle[4]+rank_singer[4]))
        self.man5.grid(row=5, column=1, columnspan=6)
        
    def click_man1(self):
        webbrowser.open_new_tab('https://www.youtube.com/results?search_query=' + str(rank_songtitle[0]) + '+' + str(rank_singer[0]))
    
    def click_eng(self):
        self.eng1 = tk.Button(self, text='英語1')
        self.eng1.grid(row=1, column=1, columnspan=6)
        self.eng2 = tk.Button(self, text='英語2')
        self.eng2.grid(row=2, column=1, columnspan=6)
        self.eng3 = tk.Button(self, text='英語3')
        self.eng3.grid(row=3, column=1, columnspan=6)
        self.eng4 = tk.Button(self, text='英語4')
        self.eng4.grid(row=4, column=1, columnspan=6)
        self.eng5 = tk.Button(self, text='英語5')
        self.eng5.grid(row=5, column=1, columnspan=6)

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