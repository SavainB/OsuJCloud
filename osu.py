try:
    import Tkinter as tk
except:
    import tkinter as tk
from ast import Load
from asyncio.windows_events import NULL
from ctypes import sizeof
from this import s
from time import sleep
import requests
import os
import mysql.connector
import time
from tkinter import Menu
from tkinter import messagebox
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from tkinter import filedialog
user_online = False
user_name =""
user_id=""
Liste_map=[]
#save all map in the directory, the argument is the link of directory
def SaveMap(str):
    for file in os.listdir(str):
        name=""
        if file[0].isdigit():
            for i in file:
                name += i;
            global Liste_map
            Liste_map.append((name,user_id))
            name =""
def save_map_offline():
    str = select_directory()
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
    messagebox.showerror("Show Example","Succesful")
def Inscription(utilisateur,password):
    if utilisateur =="" or password == "":
        messagebox.showerror("Error Example", "Something Missed")
        return None
    if len(password) <= 5 or len(utilisateur) <= 5:
        messagebox.showerror("Error Example", "Username or Password too short")
        return None
    print(utilisateur,password)
    #establishing the connection
    conn = mysql.connector.connect(user='meXh0h4eAs', password='DnjDmN3YYq', host='remotemysql.com',  port="3306", database='meXh0h4eAs')
    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM `Users`")
        data = cursor.fetchall()
        for name in data :
            if name[1] == utilisateur:
                messagebox.showerror("Error Example","Nom déja pris veuiller choisir un autre")
                return None
        # Executing the SQL command
        cursor.execute("INSERT INTO `Users` VALUES (%s, %s,%s, %s)",(None,utilisateur,password,None))
        # Commit your changes in the database
        conn.commit()
        messagebox.showerror("Show Example","compte ajouter !!!")
        master.switch_frame(Online)
    except:
        # Rolling back in case of error
        conn.rollback()
        # Closing the connection
        conn.close()
def Connexion(utilisateur,password,master):
    print(utilisateur,password)
    #establishing the connection
    conn = mysql.connector.connect(user='meXh0h4eAs', password='DnjDmN3YYq', host='remotemysql.com',  port="3306", database='meXh0h4eAs')
    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM `Users`")
        data = cursor.fetchall()
        for name in data :
            if name[1] == utilisateur:
                if name[2] == password:
                    global user_online,user_id,user_name
                    print("vous etes co")
                    messagebox.showerror("Show Example","Connection succeful !")
                    user_online=True
                    user_name=name[1]
                    user_id= str(name[0])
                    print(user_id)
                    master.switch_frame(Online_PageOne)
                    conn.commit()
                    return True
        messagebox.showerror("Error Example","Not the Password or Username")
        return None
    except:
        # Rolling back in case of error
        conn.rollback()
        # Closing the connection
        conn.close()
def download_map_online():
    conn = mysql.connector.connect(user='meXh0h4eAs', password='DnjDmN3YYq', host='remotemysql.com',  port="3306", database='meXh0h4eAs')
    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()
    tup = (Liste_map,user_id)
    try:
        sql = "SELECT name FROM List_map WHERE User_Id = %s"
        cursor.execute(sql%user_id)
        data = cursor.fetchall()
        cout=0
        des = "https://beatconnect.io/b/"
        for f in data:
            for line in f:
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
        messagebox.showerror("Show Example","Finish!")
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
        # Closing the connection
        conn.close()
def download_map_offline():
    map_link= select_file()
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
    return folder_selected
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
        messagebox.showerror("Show Example",filename)
        return filename
def ajout_map():
    select_directory()
    print(Liste_map)
    #establishing the connection
    conn = mysql.connector.connect(user='meXh0h4eAs', password='DnjDmN3YYq', host='remotemysql.com',  port="3306", database='meXh0h4eAs')
    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()
    tup = (Liste_map,user_id)
    try:
        sql = "INSERT INTO List_map (name,User_Id) VALUES (%s,%s)"
        cursor.executemany(sql,Liste_map)
        conn.commit()
        messagebox.showerror("Show Example","Finish")
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
        # Closing the connection
        conn.close()

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
        tk.Button(self,font=("Courrier",25),bg='#302727',fg='white',text='Online',width=16,height=1,command=lambda: master.switch_frame(Online)).pack(pady=10)
        tk.Button(self,font=("Courrier",25),bg='#302727',fg='white',text='Offline',width=16,height=1,command=lambda: master.switch_frame(Offline)).pack(pady=2)

class Online_Inscription(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master,bg='#302727')
        tk.Frame(self,).pack(expand=True)
        tk.Label(self,text="OSU!Cloud",font=("Courrier",40),fg='#a83d03',bg='#302727').pack(pady=9,expand=True)
        utilisateur = tk.Entry(self)
        utilisateur.pack()
        motDePasse = tk.Entry(self)
        motDePasse.pack()
        oui = tk.Button(self,font=("Courrier",25),bg='#302727',fg='white',text='Inscription',width=16,height=1,command=lambda: Inscription(str(utilisateur.get()),str(motDePasse.get())))
        oui.pack(pady=2)
        if oui:
            print("ouiiiiiiiiiiiiii")
            master.switch_frame(Online)
class Online(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master,bg='#302727')
        tk.Frame(self,).pack(expand=True)
        tk.Label(self,text="OSU!Cloud",font=("Courrier",40),fg='#a83d03',bg='#302727').pack(pady=9,expand=True)
        utilisateur = tk.Entry(self)
        utilisateur.pack()
        motDePasse = tk.Entry(self)
        motDePasse.pack()
        tk.Button(self,font=("Courrier",25),bg='#302727',fg='white',text='Connexione',width=16,height=1,command=lambda: Connexion(str(utilisateur.get()),str(motDePasse.get()),master)).pack(pady=2)
class Online_PageOne(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master,bg='#302727')
        tk.Frame.configure(self,)
        tk.Label(self,text="OSU!Cloud",font=("Courrier",40),fg='#a83d03',bg='#302727').pack(pady=9,expand=True)
        tk.Button(self,font=("Courrier",25),bg='#302727',fg='white',text='Save Your Song',width=16,height=1,command=lambda:ajout_map()).pack(pady=10)
        tk.Button(self,font=("Courrier",25),bg='#302727',fg='white',text='Have Your Song',width=16,height=1,command=lambda:download_map_online()).pack(pady=10)

class Offline(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master,bg='#302727')
        tk.Frame(self,).pack(expand=True)
        tk.Label(self,text="OSU!Cloud",font=("Courrier",40),fg='#a83d03',bg='#302727').pack(pady=9,expand=True)
        tk.Button(self,font=("Courrier",25),bg='#302727',fg='white',text='Save',width=16,height=1,command=lambda: master.switch_frame(Offline_PageOne)).pack(pady=10)
        tk.Button(self,font=("Courrier",25),bg='#302727',fg='white',text='Download',width=16,height=1,command=lambda: master.switch_frame(Offline_PageTwo)).pack(pady=2)

class Offline_PageOne(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master,bg='#302727')
        tk.Frame.configure(self,)
        tk.Label(self,text="OSU!Cloud",font=("Courrier",40),fg='#a83d03',bg='#302727').pack(pady=9,expand=True)
        tk.Button(self,font=("Courrier",25),bg='#302727',fg='white',text='Save Song',width=16,height=1,command=save_map_offline()).pack(pady=10)
        tk.Button(self,font=("Courrier",25),bg='#302727',fg='white',text='Menu',width=16,height=1,command=lambda: master.switch_frame(StartPage)).pack(pady=10)

class Offline_PageTwo(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master,bg='#302727')
        tk.Frame.configure(self,)
        tk.Label(self,text="OSU!Cloud",font=("Courrier",40),fg='#a83d03',bg='#302727').pack(pady=9,expand=True)
        tk.Button(self,font=("Courrier",25),bg='#302727',fg='white',text='Update Map',width=16,height=1,command=download_map_offline()).pack(pady=10)
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
