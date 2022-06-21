try:
    import Tkinter as tk
except:
    import tkinter as tk
from time import sleep
import requests
import os
import time
from tkinter import Menu
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from tkinter import filedialog
def SaveMap(str):
    tab=[]
    for file in os.listdir(str):
        name=""
        if file[0].isdigit():
            for i in file:
                name += i;
            tab.append(name)
            name =""
    file = open("BeatMapSave.txt","w")
    for name in tab:
        file.write(name+"\n")
def dl(map_link):
    cout=0
    des = "https://beatconnect.io/b/"
    with open(map_link) as f:
        lines = f.readlines()
        for line in lines:
            name=""
            nom=""
            cout +=1
            for i in line:
                if i.isdigit():
                    if i == " ":
                        break
                    name +=str(i)
            for i in line:
                if i =="\n":
                    break
                nom +=str(i)
            URL = des + name
            response = requests.get(URL)
            open(str(nom)+".osz", "wb").write(response.content)
            time.sleep(2)
def select_directory():
    folder_selected = filedialog.askdirectory()
    print(folder_selected)
    SaveMap(folder_selected)
def select_file():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )
    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)
    print(filename)
    dl(filename)

class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)
    
    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master,bg='#302727')
        tk.Frame(self,).pack(expand=True)
        tk.Label(self,text="OSU!Cloud",font=("Courrier",40),fg='#a83d03',bg='#302727').pack(pady=9,expand=True)
        tk.Button(self,font=("Courrier",25),bg='#302727',fg='white',text='Save',width=16,height=1,command=lambda: master.switch_frame(PageOne)).pack(pady=10)
        tk.Button(self,font=("Courrier",25),bg='#302727',fg='white',text='Download',width=16,height=1,command=lambda: master.switch_frame(PageTwo)).pack(pady=2)

class PageOne(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master,bg='#302727')
        tk.Frame.configure(self,)
        tk.Label(self,text="OSU!Cloud",font=("Courrier",40),fg='#a83d03',bg='#302727').pack(pady=9,expand=True)
        tk.Button(self,font=("Courrier",25),bg='#302727',fg='white',text='Save Song',width=16,height=1,command=select_directory).pack(pady=10)
        tk.Button(self,font=("Courrier",25),bg='#302727',fg='white',text='Menu',width=16,height=1,command=lambda: master.switch_frame(StartPage)).pack(pady=10)

class PageTwo(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master,bg='#302727')
        tk.Frame.configure(self,)
        tk.Label(self,text="OSU!Cloud",font=("Courrier",40),fg='#a83d03',bg='#302727').pack(pady=9,expand=True)
        tk.Button(self,font=("Courrier",25),bg='#302727',fg='white',text='Update Map',width=16,height=1,command=select_file).pack(pady=10)
        tk.Button(self,font=("Courrier",25),bg='#302727',fg='white',text='Menu',width=16,height=1,command=lambda: master.switch_frame(StartPage)).pack(pady=10)

if __name__ == "__main__":
    app = SampleApp()
    app.title("OSU!Cloud")
    ##root.overrideredirect(1)
    app.config(background='#302727')
    app.iconbitmap('logo.ico')
    app.resizable(False, False)
    app.geometry("340x480")
    app.mainloop()
