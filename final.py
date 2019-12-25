import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter.ttk import *
import webbrowser

url = 'https://kma.kkbox.com/charts/daily/song?cate='
song_list = ['297', '390', '308', '314', '304', '320'] # 華語man,英文eng,日文jap,韓文kor,台語twn,粵語can
song_index = -1

man_rank = []
eng_rank = []
jap_rank = []
kor_rank = []

for o in (man_rank, eng_rank, jap_rank, kor_rank):
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

def click(song, singer):
    webbrowser.open_new_tab('https://www.youtube.com/results?search_query=' + song + '+' + singer)


'''視窗'''
#logo = tk.PhotoImage(file='ppu.jpg')

class Ranking(tk.Frame):

    def __init__(self, master = None):
        tk.Frame.__init__(self, master)
        self.grid()
        #self.create_lable()
        self.create_widgets()
        self.click(man_rank)

    # 主題標籤
    # def create_lable(self):

        #self.labell = tk.label(self, image=logo)

    # 主題按鈕&名次
    def create_widgets(self): 

        self.manbut = tk.Button(self, text='華語', font="微軟正黑體", bg = 'Black', fg='White', activebackground="LightSteelBlue4", activeforeground="White", command= lambda: self.click(man_rank))
        # 這邊好像用不用lambda都沒有關係的樣子
        self.manbut.grid(row=0, column=1, ipadx=15, pady=2, sticky=tk.NW+tk.SE)
        self.engbut = tk.Button(self, text='西洋', font="微軟正黑體", bg = 'Black', fg='White', activebackground="LightSteelBlue4", activeforeground="White", command= lambda: self.click(eng_rank))
        self.engbut.grid(row=0, column=2, ipadx=15, pady=2, sticky=tk.NW+tk.SE)
        self.japbut = tk.Button(self, text='日語', font="微軟正黑體", bg = 'Black', fg='White', activebackground="LightSteelBlue4", activeforeground="White", command= lambda: self.click(jap_rank))
        self.japbut.grid(row=0, column=3, ipadx=15, pady=2, sticky=tk.NW+tk.SE)
        self.korbut = tk.Button(self, text='韓語', font="微軟正黑體", bg = 'Black', fg='White', activebackground="LightSteelBlue4", activeforeground="White", command= lambda: self.click(kor_rank))
        self.korbut.grid(row=0, column=4, ipadx=15, pady=2, sticky=tk.NW+tk.SE)

        self.rank1 = tk.Label(self, text=' 1st ', font=("微軟正黑體"), bg = 'Black', fg='Gold')
        self.rank1.grid(row=1, column=0, padx=10, pady=5, sticky=tk.NW+tk.SE)
        self.rank2 = tk.Label(self, text=' 2nd ', font=("微軟正黑體"), bg = 'Black', fg='Gold')
        self.rank2.grid(row=2, column=0, padx=10, pady=5, sticky=tk.NW+tk.SE)
        self.rank3 = tk.Label(self, text=' 3rd ', font=("微軟正黑體"), bg = 'Black', fg='Gold')
        self.rank3.grid(row=3, column=0, padx=10, pady=5, sticky=tk.NW+tk.SE)
        self.rank4 = tk.Label(self, text=' 4th ', font=("微軟正黑體"), bg = 'Black', fg='Gold')
        self.rank4.grid(row=4, column=0, padx=10, pady=5, sticky=tk.NW+tk.SE)
        self.rank5 = tk.Label(self, text=' 5th ', font=("微軟正黑體"), bg = 'Black', fg='Gold')
        self.rank5.grid(row=5, column=0, padx=10, pady=5, sticky=tk.NW+tk.SE)

    def click(self, rank_name):

        self.first = tk.Button(self, text=(rank_name[0]+ " - " + rank_name[1]), font=("微軟正黑體"), bg="Black", fg="Salmon", command= lambda: self.click_lan(rank_name, 1))
        self.first.grid(row=1, column=1, columnspan=6, sticky=tk.NW+tk.SE)
        self.second = tk.Button(self, text=(rank_name[2]+ " - " + rank_name[3]), font=("微軟正黑體"), bg="Black", fg="Salmon", command= lambda: self.click_lan(rank_name, 2))
        self.second.grid(row=2, column=1, columnspan=6, sticky=tk.NW+tk.SE)
        self.third = tk.Button(self, text=(rank_name[4]+ " - " + rank_name[5]), font=("微軟正黑體"), bg="Black", fg="Salmon", command= lambda: self.click_lan(rank_name, 3))
        self.third.grid(row=3, column=1, columnspan=6, sticky=tk.NW+tk.SE)
        self.forth = tk.Button(self, text=(rank_name[6]+ " - " + rank_name[7]), font=("微軟正黑體"), bg="Black", fg="Salmon", command= lambda: self.click_lan(rank_name, 4))
        self.forth.grid(row=4, column=1, columnspan=6, sticky=tk.NW+tk.SE)
        self.fifth = tk.Button(self, text=(rank_name[8]+ " - " + rank_name[9]), font=("微軟正黑體"), bg="Black", fg="Salmon", command= lambda: self.click_lan(rank_name, 5))
        self.fifth.grid(row=5, column=1, columnspan=6, sticky=tk.NW+tk.SE)

    def click_lan(self, language, rank):
        webbrowser.open_new_tab('https://www.youtube.com/results?search_query=' + language[rank * 2 - 2] + '+' + language[rank*2 - 1])




ranking = Ranking()
ranking.master.title("KKbox Ranking")
ranking.master.geometry('-0-50')  # 視窗設在右下角
ranking.master.attributes("-alpha",1)
ranking.master.resizable(0, 0)
ranking.configure(bg='Black')
#ranking.master.overrideredirect(True)  去邊框(上面那個)但沒辦法關
ranking.mainloop()