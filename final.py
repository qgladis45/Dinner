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
        self.click_man()

    # 主題標籤
   # def create_lable(self):

        #self.labell = tk.label(self, image=logo)

    # 主題按鈕&名次
    def create_widgets(self): 

        self.manbut = tk.Button(self, text='華語', font="微軟正黑體", bg = 'Ivory', activebackground="Cyan", activeforeground="white", command=self.click_man)
        self.manbut.grid(row=0, column=1, ipadx=15, pady=15, sticky=tk.NW+tk.SE)
        self.engbut = tk.Button(self, text='西洋', font="微軟正黑體", bg = 'Ivory', activebackground="Cyan", activeforeground="white", command=self.click_eng)
        self.engbut.grid(row=0, column=2, ipadx=15, pady=15, sticky=tk.NW+tk.SE)
        self.japbut = tk.Button(self, text='日語', font="微軟正黑體", bg = 'Ivory', activebackground="Cyan", activeforeground="white", command=self.click_jap)
        self.japbut.grid(row=0, column=3, ipadx=15, pady=15, sticky=tk.NW+tk.SE)
        self.korbut = tk.Button(self, text='韓語', font="微軟正黑體", bg = 'Ivory', activebackground="Cyan", activeforeground="white", command=self.click_kor)
        self.korbut.grid(row=0, column=4, ipadx=15, pady=15, sticky=tk.NW+tk.SE)

        self.rank1 = tk.Label(self, text=' 1st ', font=("微軟正黑體"), bg = 'Lime')
        self.rank1.grid(row=1, column=0, padx=10, pady=5, sticky=tk.NW+tk.SE)
        self.rank2 = tk.Label(self, text=' 2nd ', font=("微軟正黑體"), bg = 'Lime')
        self.rank2.grid(row=2, column=0, padx=10, pady=5, sticky=tk.NW+tk.SE)
        self.rank3 = tk.Label(self, text=' 3rd ', font=("微軟正黑體"), bg = 'Lime')
        self.rank3.grid(row=3, column=0, padx=10, pady=5, sticky=tk.NW+tk.SE)
        self.rank4 = tk.Label(self, text=' 4th ', font=("微軟正黑體"), bg = 'Lime')
        self.rank4.grid(row=4, column=0, padx=10, pady=5, sticky=tk.NW+tk.SE)
        self.rank5 = tk.Label(self, text=' 5th ', font=("微軟正黑體"), bg = 'Lime')
        self.rank5.grid(row=5, column=0, padx=10, pady=5, sticky=tk.NW+tk.SE)

    '''華語'''
    def click_man(self):
    
<<<<<<< HEAD
        self.man1 = tk.Button(self, text=(man_rank[0]+ " - " + man_rank[1]), font=("微軟正黑體"), bg="WhiteSmoke", fg="Salmon", command=self.click_man1)
        self.man1.grid(row=1, column=1, columnspan=6, padx=10, pady=5, sticky=tk.NW+tk.SE)
        self.man2 = tk.Button(self, text=(man_rank[2]+ " - " + man_rank[3]), font=("微軟正黑體"), bg="WhiteSmoke", fg="Salmon", command=self.click_man2)
        self.man2.grid(row=2, column=1, columnspan=6, padx=10, pady=5, sticky=tk.NW+tk.SE)
        self.man3 = tk.Button(self, text=(man_rank[4]+ " - " + man_rank[5]), font=("微軟正黑體"), bg="WhiteSmoke", fg="Salmon", command=self.click_man3)
        self.man3.grid(row=3, column=1, columnspan=6, padx=10, pady=5, sticky=tk.NW+tk.SE)
        self.man4 = tk.Button(self, text=(man_rank[6]+ " - " + man_rank[7]), font=("微軟正黑體"), bg="WhiteSmoke", fg="Salmon", command=self.click_man4)
        self.man4.grid(row=4, column=1, columnspan=6, padx=10, pady=5, sticky=tk.NW+tk.SE)
        self.man5 = tk.Button(self, text=(man_rank[8]+ " - " + man_rank[9]), font=("微軟正黑體"), bg="WhiteSmoke", fg="Salmon", command=self.click_man5)
        self.man5.grid(row=5, column=1, columnspan=6, padx=10, pady=5, sticky=tk.NW+tk.SE)
=======
        self.man1 = tk.Button(self, text=(man_rank[0]+man_rank[1]), font=("微軟正黑體"), bg="WhiteSmoke", height=1, width=30, fg="Salmon", command=self.click_man1)
        self.man1.grid(row=1, column=1, columnspan=6, padx=10, pady=5, sticky=tk.W)
        self.man2 = tk.Button(self, text=(man_rank[2]+man_rank[3]), font=("微軟正黑體"), bg="WhiteSmoke", height=1, width=30, fg="Salmon", command=self.click_man2)
        self.man2.grid(row=2, column=1, columnspan=6, padx=10, pady=5, sticky=tk.W)
        self.man3 = tk.Button(self, text=(man_rank[4]+man_rank[5]), font=("微軟正黑體"), bg="WhiteSmoke", height=1, width=30, fg="Salmon", command=self.click_man3)
        self.man3.grid(row=3, column=1, columnspan=6, padx=10, pady=5, sticky=tk.W)
        self.man4 = tk.Button(self, text=(man_rank[6]+man_rank[7]), font=("微軟正黑體"), bg="WhiteSmoke", height=1, width=30, fg="Salmon", command=self.click_man4)
        self.man4.grid(row=4, column=1, columnspan=6, padx=10, pady=5, sticky=tk.W)
        self.man5 = tk.Button(self, text=(man_rank[8]+man_rank[9]), font=("微軟正黑體"), bg="WhiteSmoke", height=1, width=30, fg="Salmon", command=self.click_man5)
        self.man5.grid(row=5, column=1, columnspan=6, padx=10, pady=5, sticky=tk.W)
>>>>>>> 354d9618eebbfa73e3d54c100d5ae221caea7dfa

    def click_man1(self):
        webbrowser.open_new_tab('https://www.youtube.com/results?search_query=' + man_rank[0] + '+' + man_rank[1])

    def click_man2(self):
        webbrowser.open_new_tab('https://www.youtube.com/results?search_query=' + man_rank[2] + '+' + man_rank[3])

    def click_man3(self):
        webbrowser.open_new_tab('https://www.youtube.com/results?search_query=' + man_rank[4] + '+' + man_rank[5])

    def click_man4(self):
        webbrowser.open_new_tab('https://www.youtube.com/results?search_query=' + man_rank[6] + '+' + man_rank[7])

    def click_man5(self):
        webbrowser.open_new_tab('https://www.youtube.com/results?search_query=' + man_rank[8] + '+' + man_rank[9])

    '''西洋'''
    def click_eng(self):
      
<<<<<<< HEAD
        self.eng1 = tk.Button(self, text=(eng_rank[0]+ " - " + eng_rank[1]), font=("微軟正黑體"), bg="WhiteSmoke", fg="Salmon", command=self.click_eng1)
        self.eng1.grid(row=1, column=1, columnspan=6, padx=10, pady=5, sticky=tk.NW+tk.SE)
        self.eng2 = tk.Button(self, text=(eng_rank[2]+ " - " + eng_rank[3]), font=("微軟正黑體"), bg="WhiteSmoke", fg="Salmon", command=self.click_eng2)
        self.eng2.grid(row=2, column=1, columnspan=6, padx=10, pady=5, sticky=tk.NW+tk.SE)
        self.eng3 = tk.Button(self, text=(eng_rank[4]+ " - " + eng_rank[5]), font=("微軟正黑體"), bg="WhiteSmoke", fg="Salmon", command=self.click_eng3)
        self.eng3.grid(row=3, column=1, columnspan=6, padx=10, pady=5, sticky=tk.NW+tk.SE)
        self.eng4 = tk.Button(self, text=(eng_rank[6]+ " - " + eng_rank[7]), font=("微軟正黑體"), bg="WhiteSmoke", fg="Salmon", command=self.click_eng4)
        self.eng4.grid(row=4, column=1, columnspan=6, padx=10, pady=5, sticky=tk.NW+tk.SE)
        self.eng5 = tk.Button(self, text=(eng_rank[8]+ " - " + eng_rank[9]), font=("微軟正黑體"), bg="WhiteSmoke", fg="Salmon", command=self.click_eng5)
        self.eng5.grid(row=5, column=1, columnspan=6, padx=10, pady=5, sticky=tk.NW+tk.SE)
=======
        self.eng1 = tk.Button(self, text=(eng_rank[0]+eng_rank[1]), font=("微軟正黑體"), bg="WhiteSmoke", height=1, width=30, fg="Salmon", command=self.click_eng1)
        self.eng1.grid(row=1, column=1, columnspan=6, padx=10, pady=5, sticky=tk.N)
        self.eng2 = tk.Button(self, text=(eng_rank[2]+eng_rank[3]), font=("微軟正黑體"), bg="WhiteSmoke", height=1, width=30, fg="Salmon", command=self.click_eng2)
        self.eng2.grid(row=2, column=1, columnspan=6, padx=10, pady=5, sticky=tk.N)
        self.eng3 = tk.Button(self, text=(eng_rank[4]+eng_rank[5]), font=("微軟正黑體"), bg="WhiteSmoke", height=1, width=30, fg="Salmon", command=self.click_eng3)
        self.eng3.grid(row=3, column=1, columnspan=6, padx=10, pady=5, sticky=tk.N)
        self.eng4 = tk.Button(self, text=(eng_rank[6]+eng_rank[7]), font=("微軟正黑體"), bg="WhiteSmoke", height=1, width=30, fg="Salmon", command=self.click_eng4)
        self.eng4.grid(row=4, column=1, columnspan=6, padx=10, pady=5, sticky=tk.N)
        self.eng5 = tk.Button(self, text=(eng_rank[8]+eng_rank[9]), font=("微軟正黑體"), bg="WhiteSmoke", height=1, width=30, fg="Salmon", command=self.click_eng5)
        self.eng5.grid(row=5, column=1, columnspan=6, padx=10, pady=5, sticky=tk.N)
>>>>>>> 354d9618eebbfa73e3d54c100d5ae221caea7dfa

    def click_eng1(self):
        webbrowser.open_new_tab('https://www.youtube.com/results?search_query=' + eng_rank[0] + '+' + eng_rank[1])

    def click_eng2(self):
        webbrowser.open_new_tab('https://www.youtube.com/results?search_query=' + eng_rank[2] + '+' + eng_rank[3])

    def click_eng3(self):
        webbrowser.open_new_tab('https://www.youtube.com/results?search_query=' + eng_rank[4] + '+' + eng_rank[5])

    def click_eng4(self):
        webbrowser.open_new_tab('https://www.youtube.com/results?search_query=' + eng_rank[6] + '+' + eng_rank[7])

    def click_eng5(self):
        webbrowser.open_new_tab('https://www.youtube.com/results?search_query=' + eng_rank[8] + '+' + eng_rank[9])

    '''日語'''
    def click_jap(self):
    
<<<<<<< HEAD
        self.jap1 = tk.Button(self, text=(jap_rank[0]+ " - " + jap_rank[1]), font=("微軟正黑體"), bg="WhiteSmoke", fg="Salmon", command=self.click_jap1)
        self.jap1.grid(row=1, column=1, columnspan=6, padx=10, pady=5, sticky=tk.NW+tk.SE)
        self.jap2 = tk.Button(self, text=(jap_rank[2]+ " - " + jap_rank[3]), font=("微軟正黑體"), bg="WhiteSmoke", fg="Salmon", command=self.click_jap2)
        self.jap2.grid(row=2, column=1, columnspan=6, padx=10, pady=5, sticky=tk.NW+tk.SE)
        self.jap3 = tk.Button(self, text=(jap_rank[4]+ " - " + jap_rank[5]), font=("微軟正黑體"), bg="WhiteSmoke", fg="Salmon", command=self.click_jap3)
        self.jap3.grid(row=3, column=1, columnspan=6, padx=10, pady=5, sticky=tk.NW+tk.SE)
        self.jap4 = tk.Button(self, text=(jap_rank[6]+ " - " + jap_rank[7]), font=("微軟正黑體"), bg="WhiteSmoke", fg="Salmon", command=self.click_jap4)
        self.jap4.grid(row=4, column=1, columnspan=6, padx=10, pady=5, sticky=tk.NW+tk.SE)
        self.jap5 = tk.Button(self, text=(jap_rank[8]+ " - " + jap_rank[9]), font=("微軟正黑體"), bg="WhiteSmoke", fg="Salmon", command=self.click_jap5)
        self.jap5.grid(row=5, column=1, columnspan=6, padx=10, pady=5, sticky=tk.NW+tk.SE)
=======
        self.jap1 = tk.Button(self, text=(jap_rank[0]+jap_rank[1]), font=("微軟正黑體"), bg="WhiteSmoke", height=1, width=30, fg="Salmon", command=self.click_jap1)
        self.jap1.grid(row=1, column=1, columnspan=6, padx=10, pady=5, sticky=tk.N)
        self.jap2 = tk.Button(self, text=(jap_rank[2]+jap_rank[3]), font=("微軟正黑體"), bg="WhiteSmoke", height=1, width=30, fg="Salmon", command=self.click_jap2)
        self.jap2.grid(row=2, column=1, columnspan=6, padx=10, pady=5, sticky=tk.N)
        self.jap3 = tk.Button(self, text=(jap_rank[4]+jap_rank[5]), font=("微軟正黑體"), bg="WhiteSmoke", height=1, width=30, fg="Salmon", command=self.click_jap3)
        self.jap3.grid(row=3, column=1, columnspan=6, padx=10, pady=5, sticky=tk.N)
        self.jap4 = tk.Button(self, text=(jap_rank[6]+jap_rank[7]), font=("微軟正黑體"), bg="WhiteSmoke", height=1, width=30, fg="Salmon", command=self.click_jap4)
        self.jap4.grid(row=4, column=1, columnspan=6, padx=10, pady=5, sticky=tk.N)
        self.jap5 = tk.Button(self, text=(jap_rank[8]+jap_rank[9]), font=("微軟正黑體"), bg="WhiteSmoke", height=1, width=30, fg="Salmon", command=self.click_jap5)
        self.jap5.grid(row=5, column=1, columnspan=6, padx=10, pady=5, sticky=tk.N)
>>>>>>> 354d9618eebbfa73e3d54c100d5ae221caea7dfa

    def click_jap1(self):
        webbrowser.open_new_tab('https://www.youtube.com/results?search_query=' + jap_rank[0] + '+' + jap_rank[1])

    def click_jap2(self):
        webbrowser.open_new_tab('https://www.youtube.com/results?search_query=' + jap_rank[2] + '+' + jap_rank[3])

    def click_jap3(self):
        webbrowser.open_new_tab('https://www.youtube.com/results?search_query=' + jap_rank[4] + '+' + jap_rank[5])

    def click_jap4(self):
        webbrowser.open_new_tab('https://www.youtube.com/results?search_query=' + jap_rank[6] + '+' + jap_rank[7])

    def click_jap5(self):
        webbrowser.open_new_tab('https://www.youtube.com/results?search_query=' + jap_rank[8] + '+' + jap_rank[9])

    '''韓語'''
    def click_kor(self):
    
<<<<<<< HEAD
        self.kor1 = tk.Button(self, text=(kor_rank[0]+ " - " + kor_rank[1]), font=("微軟正黑體"), bg="WhiteSmoke", fg="Salmon", command=self.click_kor1)
        self.kor1.grid(row=1, column=1, columnspan=6, padx=10, pady=5, sticky=tk.NW+tk.SE)
        self.kor2 = tk.Button(self, text=(kor_rank[2]+ " - " + kor_rank[3]), font=("微軟正黑體"), bg="WhiteSmoke", fg="Salmon", command=self.click_kor2)
        self.kor2.grid(row=2, column=1, columnspan=6, padx=10, pady=5, sticky=tk.NW+tk.SE)
        self.kor3 = tk.Button(self, text=(kor_rank[4]+ " - " + kor_rank[5]), font=("微軟正黑體"), bg="WhiteSmoke", fg="Salmon", command=self.click_kor3)
        self.kor3.grid(row=3, column=1, columnspan=6, padx=10, pady=5, sticky=tk.NW+tk.SE)
        self.kor4 = tk.Button(self, text=(kor_rank[6]+ " - " + kor_rank[7]), font=("微軟正黑體"), bg="WhiteSmoke", fg="Salmon", command=self.click_kor4)
        self.kor4.grid(row=4, column=1, columnspan=6, padx=10, pady=5, sticky=tk.NW+tk.SE)
        self.kor5 = tk.Button(self, text=(kor_rank[8]+ " - " + kor_rank[9]), font=("微軟正黑體"), bg="WhiteSmoke", fg="Salmon", command=self.click_kor5)
        self.kor5.grid(row=5, column=1, columnspan=6, padx=10, pady=5, sticky=tk.NW+tk.SE)
=======
        self.kor1 = tk.Button(self, text=(kor_rank[0]+kor_rank[1]), font=("微軟正黑體"), bg="WhiteSmoke", height=1, width=30, fg="Salmon", command=self.click_kor1)
        self.kor1.grid(row=1, column=1, columnspan=6, padx=10, pady=5, sticky=tk.N)
        self.kor2 = tk.Button(self, text=(kor_rank[2]+kor_rank[3]), font=("微軟正黑體"), bg="WhiteSmoke", height=1, width=30, fg="Salmon", command=self.click_kor2)
        self.kor2.grid(row=2, column=1, columnspan=6, padx=10, pady=5, sticky=tk.N)
        self.kor3 = tk.Button(self, text=(kor_rank[4]+kor_rank[5]), font=("微軟正黑體"), bg="WhiteSmoke", height=1, width=30, fg="Salmon", command=self.click_kor3)
        self.kor3.grid(row=3, column=1, columnspan=6, padx=10, pady=5, sticky=tk.N)
        self.kor4 = tk.Button(self, text=(kor_rank[6]+kor_rank[7]), font=("微軟正黑體"), bg="WhiteSmoke", height=1, width=30, fg="Salmon", command=self.click_kor4)
        self.kor4.grid(row=4, column=1, columnspan=6, padx=10, pady=5, sticky=tk.N)
        self.kor5 = tk.Button(self, text=(kor_rank[8]+kor_rank[9]), font=("微軟正黑體"), bg="WhiteSmoke", height=1, width=30, fg="Salmon", command=self.click_kor5)
        self.kor5.grid(row=5, column=1, columnspan=6, padx=10, pady=5, sticky=tk.N)
>>>>>>> 354d9618eebbfa73e3d54c100d5ae221caea7dfa

    def click_kor1(self):
        webbrowser.open_new_tab('https://www.youtube.com/results?search_query=' + kor_rank[0] + '+' + kor_rank[1])

    def click_kor2(self):
        webbrowser.open_new_tab('https://www.youtube.com/results?search_query=' + kor_rank[2] + '+' + kor_rank[3])

    def click_kor3(self):
        webbrowser.open_new_tab('https://www.youtube.com/results?search_query=' + kor_rank[4] + '+' + kor_rank[5])

    def click_kor4(self):
        webbrowser.open_new_tab('https://www.youtube.com/results?search_query=' + kor_rank[6] + '+' + kor_rank[7])

    def click_kor5(self):
        webbrowser.open_new_tab('https://www.youtube.com/results?search_query=' + kor_rank[8] + '+' + kor_rank[9])

ranking = Ranking()
ranking.master.title("KKbox Ranking")
#ranking.master.geometry('400x200')
ranking.master.attributes("-alpha",1)
ranking.master.resizable(0, 0)
ranking.mainloop()