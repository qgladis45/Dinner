import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
import webbrowser
from PIL import Image, ImageTk
from urllib.request import urlopen
import io

#網路連線檢查
def popup_showinfo():
    showinfo("溫馨小提示", "NO INTERNET CONNECTION") 

def check_internet():
    url='http://www.google.com/'
    timeout=5
    try:
        _ = requests.get(url, timeout=timeout) #以谷歌測試
        return True
    except requests.ConnectionError:
        popup_showinfo() #如果沒網路，以視窗顯示
    return False
check_internet()
	
'''爬蟲'''
url = "https://kma.kkbox.com/charts/daily/song?cate="
song_list = ['297', '390', '308', '314']  # 華語man, 英文eng, 日文jap, 韓文kor
song_index = -1

man_rank = []
eng_rank = []
jap_rank = []
kor_rank = []

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

for o in (man_rank, eng_rank, jap_rank, kor_rank):
    song_index += 1
    song_url = url + song_list[song_index]

    r = requests.get(song_url)

    soup = BeautifulSoup(r.text, 'html.parser')
    attr = {'name': 'description'}

    rank = soup.find_all('meta', attrs=attr)     # 找到html裡面的meta標籤
    rank_str = rank[0]['content']                  # 找到排行榜的部分
    rank_str = rank_str[(rank_str.find('：')+1):]  # 只抓取歌單的部分
    rank_list = rank_str.split('、')               # 把str轉成list

    # list中0,2,4,6,8為歌名; 1,3,5,7,9為歌手
    for i in rank_list:
        # rank = i.strip()
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

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.create_widgets()
        self.click(man_rank)

    # 建立主題按鈕&名次
    def create_widgets(self):

        # 主題(button)
        self.manbut = tk.Button(self, text="華語", font='微軟正黑體', bg='Black', fg='White', activebackground='LightSteelBlue4', activeforeground='White', command=(lambda: self.click(man_rank)))
        self.manbut.grid(row=0, column=2, ipadx=15, pady=2, sticky=(tk.NW+tk.SE))
        self.engbut = tk.Button(self, text="西洋", font='微軟正黑體', bg='Black', fg='White', activebackground='LightSteelBlue4', activeforeground='White', command=(lambda: self.click(eng_rank)))
        self.engbut.grid(row=0, column=3, ipadx=15, pady=2, sticky=(tk.NW+tk.SE))
        self.japbut = tk.Button(self, text="日語", font='微軟正黑體', bg='Black', fg='White', activebackground='LightSteelBlue4', activeforeground='White', command=(lambda: self.click(jap_rank)))
        self.japbut.grid(row=0, column=4, ipadx=15, pady=2, sticky=(tk.NW+tk.SE))
        self.korbut = tk.Button(self, text="韓語", font='微軟正黑體', bg='Black', fg='White', activebackground='LightSteelBlue4', activeforeground='White', command=(lambda: self.click(kor_rank)))
        self.korbut.grid(row=0, column=5, ipadx=15, pady=2, sticky=(tk.NW+tk.SE))

        # 名次(label)
        self.rank1 = tk.Label(self, text=' 1st ', font='微軟正黑體', bg='Black', fg='Gold')
        self.rank1.grid(row=1, column=0, padx=10, pady=5, sticky=(tk.NW+tk.SE))
        self.rank2 = tk.Label(self, text=' 2nd ', font='微軟正黑體', bg='Black', fg='Gold')
        self.rank2.grid(row=2, column=0, padx=10, pady=5, sticky=(tk.NW+tk.SE))
        self.rank3 = tk.Label(self, text=' 3rd ', font='微軟正黑體', bg='Black', fg='Gold')
        self.rank3.grid(row=3, column=0, padx=10, pady=5, sticky=(tk.NW+tk.SE))
        self.rank4 = tk.Label(self, text=' 4th ', font='微軟正黑體', bg='Black', fg='Gold')
        self.rank4.grid(row=4, column=0, padx=10, pady=5, sticky=(tk.NW+tk.SE))
        self.rank5 = tk.Label(self, text=' 5th ', font='微軟正黑體', bg='Black', fg='Gold')
        self.rank5.grid(row=5, column=0, padx=10, pady=5, sticky=(tk.NW+tk.SE))

        # 離開(button)
        self.exitbut = tk.Button(self, width=2, text='Ⓧ', font=('微軟正黑體', 12), bg='Black', fg='Gray55', activebackground='Black', activeforeground='red', relief='flat', command=(lambda: self.quit()))
        self.exitbut.grid(row=0, column=0, sticky=tk.NW)


    # function: 各主題的排行(button)
    def click(self, rank_name):
        self.but1 = tk.Button(self, text=(rank_name[0] + " - " + rank_name[1]), font='微軟正黑體', bg='Black', fg='Snow2', activebackground='LightSteelBlue4', activeforeground='White', command=(lambda: self.click_lan(rank_name, 1)))
        self.but1.grid(row=1, column=2, columnspan=6, sticky=(tk.NW+tk.SE))
        self.but2 = tk.Button(self, text=(rank_name[2] + " - " + rank_name[3]), font='微軟正黑體', bg='Black', fg='Snow2', activebackground='LightSteelBlue4', activeforeground='White', command=(lambda: self.click_lan(rank_name, 2)))
        self.but2.grid(row=2, column=2, columnspan=6, sticky=(tk.NW+tk.SE))
        self.but3 = tk.Button(self, text=(rank_name[4] + " - " + rank_name[5]), font='微軟正黑體', bg='Black', fg='Snow2', activebackground='LightSteelBlue4', activeforeground='White', command=(lambda: self.click_lan(rank_name, 3)))
        self.but3.grid(row=3, column=2, columnspan=6, sticky=(tk.NW+tk.SE))
        self.but4 = tk.Button(self, text=(rank_name[6] + " - " + rank_name[7]), font='微軟正黑體', bg='Black', fg='Snow2', activebackground='LightSteelBlue4', activeforeground='White', command=(lambda: self.click_lan(rank_name, 4)))
        self.but4.grid(row=4, column=2, columnspan=6, sticky=(tk.NW+tk.SE))
        self.but5 = tk.Button(self, text=(rank_name[8] + " - " + rank_name[9]), font='微軟正黑體', bg='Black', fg='Snow2', activebackground='LightSteelBlue4', activeforeground='White', command=(lambda: self.click_lan(rank_name, 5)))
        self.but5.grid(row=5, column=2, columnspan=6, sticky=(tk.NW+tk.SE))

        # 圖片
        self.url = requests.get(man_cover[3])
        self.imagebyte = io.BytesIO(self.url.content)
        self.imagepil = Image.open(self.imagebyte)
        self.imagepil = self.imagepil.resize((80, 80), Image.ANTIALIAS)  # 重設大小
        self.image1 = ImageTk.PhotoImage(self.imagepil)

        # 圖片(Label)
        self.pic1 = tk.Label(self, image=self.image1, bg='Black')
        self.pic1.grid(row=1, column=1, sticky=(tk.NW+tk.SE))
        self.pic2 = tk.Label(self, image=self.image1, bg='Black')
        self.pic2.grid(row=2, column=1, sticky=(tk.NW+tk.SE))
        self.pic3 = tk.Label(self, image=self.image1, bg='Black')
        self.pic3.grid(row=3, column=1, sticky=(tk.NW+tk.SE))
        self.pic4 = tk.Label(self, image=self.image1, bg='Black')
        self.pic4.grid(row=4, column=1, sticky=(tk.NW+tk.SE))
        self.pic5 = tk.Label(self, image=self.image1, bg='Black')
        self.pic5.grid(row=5, column=1, sticky=(tk.NW+tk.SE))

    # function: 按下歌曲
    def click_lan(self, language, rank):
        webbrowser.open_new_tab("https://www.youtube.com/results?search_query=" + language[rank*2 - 2] + "+" + language[rank*2 - 1])  # 開啟Youtube搜尋頁面

ranking = Ranking()
ranking.master.title("KKbox Ranking")
ranking.master.geometry('-30-50')      # 視窗設在右下角
ranking.master.attributes('-alpha', 1)  # 不透明
ranking.master.resizable(0, 0)         # 鎖定視窗大小
ranking.configure(bg='Black')          # 背景顏色
ranking.master.overrideredirect(True)  # 刪除標題欄
ranking.mainloop()
