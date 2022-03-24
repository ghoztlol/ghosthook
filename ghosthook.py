"""
--------------------------------------------------------

██████╗░░█████╗░░█████╗░██╗░░██╗░█████╗░░█████╗░██╗░░██╗
██╔══██╗██╔══██╗██╔══██╗██║░░██║██╔══██╗██╔══██╗██║░██╔╝
██████╦╝██║░░██║██║░░██║███████║██║░░██║██║░░██║█████═╝░
██╔══██╗██║░░██║██║░░██║██╔══██║██║░░██║██║░░██║██╔═██╗░
██████╦╝╚█████╔╝╚█████╔╝██║░░██║╚█████╔╝╚█████╔╝██║░╚██╗
╚═════╝░░╚════╝░░╚════╝░╚═╝░░╚═╝░╚════╝░░╚════╝░╚═╝░░╚═╝

--------------------------------------------------------

ghozt#0002
"""
import os
import re
import win32gui
import win32console                                                                                                
import threading
import requests
from time import sleep
from tkinter import *
from tkinter import messagebox
from colorama import Fore, init
from discord_webhook import DiscordEmbed, DiscordWebhook

init()

window = Tk()
window.title("ghosthook")
window.geometry("700x550")
window.maxsize(700, 550)
window.minsize(700, 550)
window.iconbitmap("assets/ghost.ico")
window.config(background='#484848')

# importing images
bacg = PhotoImage(file='assets/background.png')
colorbg = PhotoImage(file='assets/colorbg.png')
choosebu = PhotoImage(file='assets/img1.png')
startbu = PhotoImage(file='assets/img0.png')
blankbu = PhotoImage(file='assets/blankbu.png')
fullbu = PhotoImage(file='assets/fullbu.png')
blk = PhotoImage(file='assets/blk.png')
blu = PhotoImage(file='assets/blu.png')
blk = PhotoImage(file='assets/blk.png')
dblu = PhotoImage(file='assets/dblu.png')
dr = PhotoImage(file='assets/dr.png')
green = PhotoImage(file='assets/green.png')
grey = PhotoImage(file='assets/grey.png')
ng = PhotoImage(file='assets/ng.png')
npink = PhotoImage(file='assets/npink.png')
o = PhotoImage(file='assets/o.png')
pb = PhotoImage(file='assets/pb.png')
pblu = PhotoImage(file='assets/pblu.png')
pg = PhotoImage(file='assets/pg.png')
pink = PhotoImage(file='assets/pink.png')
pm = PhotoImage(file='assets/pm.png')
pp = PhotoImage(file='assets/pp.png')
pur = PhotoImage(file='assets/pur.png')
py = PhotoImage(file='assets/py.png')
r = PhotoImage(file='assets/r.png')
turq = PhotoImage(file='assets/turq.png')
w = PhotoImage(file='assets/w.png')
y = PhotoImage(file='assets/y.png')

os.system("mode con cols=62 lines=22")
os.system("title " + "ghost-hook logs")

class ghosthook:
    def __init__(self):
        os.system("cls")
        self.delwbhison = False
        self.hideconon = False
        self.iscolorchose = ''
        print(Fore.WHITE+"""


██████╗░░█████╗░░█████╗░██╗░░██╗░█████╗░░█████╗░██╗░░██╗
██╔══██╗██╔══██╗██╔══██╗██║░░██║██╔══██╗██╔══██╗██║░██╔╝
██████╦╝██║░░██║██║░░██║███████║██║░░██║██║░░██║█████═╝░
██╔══██╗██║░░██║██║░░██║██╔══██║██║░░██║██║░░██║██╔═██╗░
██████╦╝╚█████╔╝╚█████╔╝██║░░██║╚█████╔╝╚█████╔╝██║░╚██╗
╚═════╝░░╚════╝░░╚════╝░╚═╝░░╚═╝░╚════╝░░╚════╝░╚═╝░░╚═╝

--------------------------------------------------------

ghozt#0002
        """)
        print(Fore.RED+"["+Fore.WHITE+"+"+Fore.RED+"]"+Fore.WHITE+" logs")
        self.webhookspamndeletemain()
    
    def delwbhon(self):
        if self.delwbhison == False:
            self.delwbhison = True
            self.delewbh.config(image=fullbu)
        else:
            self.delwbhison = False
            self.delewbh.config(image=blankbu)
    def hidd(self):
        if self.hideconon == False:
            self.hideconon = True
            self.hidecon.config(image=fullbu)
            win = win32console.GetConsoleWindow()
            win32gui.ShowWindow(win, 0)
        else:
            self.hideconon = False
            self.hidecon.config(image=blankbu)
            win = win32console.GetConsoleWindow()
            win32gui.ShowWindow(win, 1)
    
    def justsendwebh(self):
        hellobitch = False
        webhook = self.dadvwebhook.get()
        try:
            amount = int(self.dadvamount.get())
        except:
            messagebox.showerror('ghost-hook | ghozt#0002', 'invalid amount')
            self.__init__()
        content= self.dadvcontent.get()
        if self.delwbhison == False:
            for i in range(amount):
                r = requests.post(webhook, json={'content' : f'{content}'})
                if r.status_code == 429:
                    sleep(10)
                if r.status_code ==404:
                    messagebox.showerror('ghost-hook | ghozt#0002', 'invalid webhook')
                    self.__init__()
                    hellobitch = True
                    break
                if r.status_code == 200:
                    print(Fore.YELLOW+"["+Fore.WHITE+"LOG"+Fore.YELLOW+"]"+Fore.WHITE+f" message sent")
                sleep(0.1)
            if hellobitch == True:
                pass
            else:
                print(Fore.YELLOW+"["+Fore.WHITE+"LOG"+Fore.YELLOW+"]"+Fore.WHITE+f" successfully spammed the webhook!")
                messagebox.showinfo('ghost-hook | ghozt#0002', 'successfully spammed the webhook !')
                self.__init__()
        else:
            for i in range(amount):
                r = requests.post(webhook, json={'content' : f'{content}'})
                if r.status_code == 429:
                    sleep(10)
                if r.status_code ==404:
                    messagebox.showerror('ghost-hook | ghozt#0002', 'invalid webhook')
                    self.__init__()
                    hellobitch = True
                    break
                if r.status_code == 200:
                    print(Fore.YELLOW+"["+Fore.WHITE+"LOG"+Fore.YELLOW+"]"+Fore.WHITE+f" message sent")
            if hellobitch == True:
                pass
            else:
                x = requests.delete(webhook)
                print(Fore.YELLOW+"["+Fore.WHITE+"LOG"+Fore.YELLOW+"]"+Fore.WHITE+f" successfully deleted and spammed the webhook!")
                messagebox.showinfo('ghost-hook | ghozt#0002', 'successfully deleted and spammed the webhook!')
                
                self.__init__()

    def checkdelorfuckoff(self):
        if self.delwbhison == True:
            webhook = self.dadvwebhook.get()
            x = requests.delete(webhook)
            print(Fore.YELLOW+"["+Fore.WHITE+"LOG"+Fore.YELLOW+"]"+Fore.WHITE+f" webhook deleted")
            messagebox.showinfo('ghost-hook | ghozt#0002', 'successfully deleted the webhook!')
            self.__init__()
        else:
            messagebox.showinfo('ghost-hook | ghozt#0002', 'no actions have been selected')
            self.__init__()

    def dadvsendwb(self):
        hellobitch = False
        amonn = 0
        webhookz = self.dadvwebhook.get()
        contentz = self.dadvcontent.get()
        amountz = int(self.dadvamount.get())
        usernamez = self.dadvusername.get()
        avatar_urlz = self.dadvavatarurl.get()
        titlez = self.dadvtitle.get()
        descz = self.dadvdesc.get()
        colorz = self.iscolorchose
        authorz = self.dadvauthor.get()
        footerz = self.dadvfooter.get()
        gifz = self.dadvgif.get()
        for i in range(amountz):
            content = contentz
            webhook = DiscordWebhook(url=webhookz, username=usernamez, avatar_url=avatar_urlz,content=content)
            embed = DiscordEmbed(title=titlez, description=descz, color=colorz)
            embed.set_author(name=authorz)
            embed.set_footer(text=footerz)
            embed.set_timestamp()
            embed.set_image(url=gifz)
            webhook.add_embed(embed)
            response = webhook.execute()
            if response.status_code == 429:
                sleep(10)
            if response.status_code == 200:
                print(Fore.YELLOW+"["+Fore.WHITE+"LOG"+Fore.YELLOW+"]"+Fore.WHITE+f" message sent")
            if response.status_code == 404:
                messagebox.showerror('ghost-hook | ghozt#0002', 'invalid webhook')
                self.__init__()
                hellobitch = True
                break
        if hellobitch == True:
            pass
        else:
            if self.delwbhison == True:
                x = requests.delete(webhookz)
                print(Fore.YELLOW+"["+Fore.WHITE+"LOG"+Fore.YELLOW+"]"+Fore.WHITE+f" successfully spammed and deleted the webhook!")
                messagebox.showinfo('ghost-hook | ghozt#0002', 'successfully spammed and deleted the webhook!')
                    
                self.__init__()
            else:
                print(Fore.YELLOW+"["+Fore.WHITE+"LOG"+Fore.YELLOW+"]"+Fore.WHITE+f" successfully spammed the webhook !")
                messagebox.showinfo('ghost-hook | ghozt#0002', 'successfully spammed the webhook !')
                self.__init__()

    def dadvverification(self):
        poop_lol = None
        self.embedon = 0
        username = self.dadvusername.get()
        avatar_url = self.dadvavatarurl.get()
        title = self.dadvtitle.get()
        desc = self.dadvdesc.get()
        author = self.dadvauthor.get()
        footer = self.dadvfooter.get()
        gif = self.dadvgif.get()
        if len(username) >0:
            self.embedon +=1
        else:
            pass
        if len(avatar_url) >0:
            self.embedon +=1
        else:
            pass
        if len(title) >0:
            self.embedon +=1
        else:
            pass
        if len(desc) >0:
            self.embedon +=1
        else:
            pass
        if len(author) >0:
            self.embedon +=1
        else:
            pass
        if len(footer) >0:
            self.embedon +=1
        else:
            pass
        if len(gif) >0:
            self.embedon +=1
        else:
            pass
        if self.embedon > 0:
            poop_lol =True
        else:
            poop_lol = False
        if poop_lol == True:
            itworkslol = False
            while True:
                webhook = self.dadvwebhook.get()
                if webhook.startswith('https://discord.com/api/webhooks/') or webhook.startswith('https://discordapp.com/api/webhooks/'):
                    r = requests.get(webhook)
                    if r.status_code == 200:
                        itworkslol = True
                    else:
                        itworkslol = False
                        messagebox.showerror('ghost-hook | ghozt#0002', 'invalid webhook')
                        break
                else:
                    itworkslol = False
                    messagebox.showerror('ghost-hook | ghozt#0002', 'invalid webhook')
                    break
                content = self.dadvcontent.get()
                if len(content) > 0:
                    itworkslol = True
                    print(Fore.YELLOW+"["+Fore.WHITE+"+"+Fore.YELLOW+"]"+Fore.WHITE+f" Content : {content}")
                else:
                    itworkslol = False
                    messagebox.showerror('ghost-hook | ghozt#0002', 'fill out content!')
                    break
                try:
                    amount = int(self.dadvamount.get())
                    if amount > 0:
                        itworks = True
                        print(Fore.YELLOW+"["+Fore.WHITE+"+"+Fore.YELLOW+"]"+Fore.WHITE+f" amount : {amount}")
                    else:
                        itworkslol = False
                        messagebox.showerror('ghost-hook | ghozt#0002', 'invalid amount')
                        break
                except:
                        itworkslol = False
                        messagebox.showerror('ghost-hook | ghozt#0002', 'invalid amount')
                        break
                username = self.dadvusername.get()
                if len(username) > 0:
                    self.embedon +=1
                    itworkslol = True
                    print(Fore.YELLOW+"["+Fore.WHITE+"+"+Fore.YELLOW+"]"+Fore.WHITE+f" username : {username}")
                else:
                    itworkslol = False
                    messagebox.showerror('ghost-hook | ghozt#0002', 'fill out username!')
                    break
                avatar_url = self.dadvavatarurl.get()
                if len(avatar_url) > 0:
                    if avatar_url.startswith('https://cdn.discordapp.com/'):
                        self.embedon +=1
                        itworkslol = True
                        print(Fore.YELLOW+"["+Fore.WHITE+"+"+Fore.YELLOW+"]"+Fore.WHITE+f" avatar URL : {avatar_url}")
                    else:
                        itworkslol = False
                        messagebox.showerror('ghost-hook | ghozt#0002', 'invalid cnd attachement for avatar URL')
                        break
                else:
                    itworkslol = False
                    messagebox.showerror('ghost-hook | ghozt#0002', 'fill out avatar_url!')
                    break
                title = self.dadvtitle.get()
                if len(title) > 0:
                    self.embedon +=1
                    itworkslol = True
                    print(Fore.YELLOW+"["+Fore.WHITE+"+"+Fore.YELLOW+"]"+Fore.WHITE+f" title : {title}")
                else:
                    itworkslol = False
                    messagebox.showerror('ghost-hook | ghozt#0002', 'fill out title!')
                    break
                desc = self.dadvdesc.get()
                if len(desc) > 0:
                    self.embedon +=1
                    itworkslol = True
                    print(Fore.YELLOW+"["+Fore.WHITE+"+"+Fore.YELLOW+"]"+Fore.WHITE+f" description : {desc}")
                else:
                    itworkslol = False
                    messagebox.showerror('ghost-hook | ghozt#0002', 'fill out description !')
                    break
                color = self.iscolorchose
                if color != None:
                    self.embedon +=1
                    itworkslol = True
                    print(Fore.YELLOW+"["+Fore.WHITE+"+"+Fore.YELLOW+"]"+Fore.WHITE+f" color : {color}")
                else:
                    itworkslol = False
                    messagebox.showerror('ghost-hook | ghozt#0002', 'invalid color')
                    break
                author = self.dadvauthor.get()
                if len(author) > 0:
                    self.embedon +=1
                    itworkslol = True
                    print(Fore.YELLOW+"["+Fore.WHITE+"+"+Fore.YELLOW+"]"+Fore.WHITE+f" author : {author}")
                else:
                    itworkslol = False
                    messagebox.showerror('ghost-hook | ghozt#0002', 'fill out author!')
                    break
                footer = self.dadvfooter.get()
                if len(footer) > 0:
                    self.embedon +=1
                    itworkslol = True
                    print(Fore.YELLOW+"["+Fore.WHITE+"+"+Fore.YELLOW+"]"+Fore.WHITE+f" footer : {footer}")
                else:
                    itworkslol = False
                    messagebox.showerror('ghost-hook | ghozt#0002', 'fill out footer!')
                    break
                gif = self.dadvgif.get()
                if len(gif) > 0:
                    self.embedon +=1
                    if gif.startswith('https://cdn.discordapp.com/'):
                        itworkslol = True
                        print(Fore.YELLOW+"["+Fore.WHITE+"+"+Fore.YELLOW+"]"+Fore.WHITE+f" gif/img : {gif}")
                    else:
                        itworkslol = False
                        messagebox.showerror('ghost-hook | ghozt#0002', 'invalid')
                        break
                else:
                    itworkslol = False
                    messagebox.showerror('ghost-hook | ghozt#0002', 'invalid cnd attachement for gif / image')
                    break
                if itworkslol == True:
                    break
            if itworkslol == True:
                t1 = threading.Thread(target=self.dadvsendwb)
                t1.start()
            else:
                self.__init__()
        else:
            poopy_head = None
            wtf_is_this = 0
            while True:
                webhook = self.dadvwebhook.get()
                content = self.dadvcontent.get()
                if len(webhook) > 0:
                    wtf_is_this +=1
                    r = requests.get(webhook)
                    if r.status_code == 200:
                        pass
                    else:
                        messagebox.showerror('ghost-hook | ghozt#0002', 'invalid Webhook')
                        poopy_head = False
                        break
                else:
                    pass
                if len(content) > 0:
                    wtf_is_this +=1
                else:
                    pass
                try:
                    amount2 = int(self.dadvamount.get())
                    if amount2 > 0:
                        wtf_is_this +=1
                    else:
                        pass
                except:
                    pass
                poopy_head = True
                break
            if poopy_head == True:
                if wtf_is_this <= 2:
                    t2 = threading.Thread(target=self.checkdelorfuckoff)
                    t2.start()
                else:
                    t2 = threading.Thread(target=self.justsendwebh)
                    t2.start()
            else:
                self.webhookspamndeletemain()

    def blk1(self):
        self.iscolorchose ='2B2B2B'
        self.webhookspamndeletemain()
    def blu1(self):
        self.iscolorchose ='0085FF'
        self.webhookspamndeletemain()
    def dblu1(self):
        self.iscolorchose ='1400FF'
        self.webhookspamndeletemain()
    def dr1(self):
        self.iscolorchose ='780000'
        self.webhookspamndeletemain()
    def green1(self):
        self.iscolorchose ='027100'
        self.webhookspamndeletemain()
    def grey1(self):
        self.iscolorchose ='989898'
        self.webhookspamndeletemain()
    def ng1(self):
        self.iscolorchose ='ADFF00'
        self.webhookspamndeletemain()
    def npink1(self):
        self.iscolorchose ='BD00FF'
        self.webhookspamndeletemain()
    def o1(self):
        self.iscolorchose ='FF7A00'
        self.webhookspamndeletemain()
    def pb1(self):
        self.iscolorchose ='00FF85'
        self.webhookspamndeletemain()
    def pblu1(self):
        self.iscolorchose ='00F0FF'
        self.webhookspamndeletemain()
    def pg1(self):
        self.iscolorchose ='00FF85'
        self.webhookspamndeletemain()
    def pink1(self):
        self.iscolorchose ='FF006B'
        self.webhookspamndeletemain()
    def pm1(self):
        self.iscolorchose ='8684FF'
        self.webhookspamndeletemain()
    def pp1(self):
        self.iscolorchose ='FF84CE'
        self.webhookspamndeletemain()
    def pur1(self):
        self.iscolorchose ='7000FF'
        self.webhookspamndeletemain()
    def py1(self):
        self.iscolorchose ='FFDC84'
        self.webhookspamndeletemain()
    def r1(self):
        self.iscolorchose ='FF0000'
        self.webhookspamndeletemain()
    def turq1(self):
        self.iscolorchose ='00716A'
        self.webhookspamndeletemain()
    def w1(self):
        self.iscolorchose ='FFFFFF'
        self.webhookspamndeletemain()
    def y1(self):
        self.iscolorchose ='FFC700'
        self.webhookspamndeletemain()

    def colormain(self):
        bkkk = Label(window, image=colorbg, borderwidth=0)
        bkkk.place(x=0,y=0)
        blkbu = Button(window, image=blk,bg='#484848',borderwidth=0, activebackground="#484848",command=self.blk1)
        blkbu.place(x=185,y=236)
        blubu = Button(window, image=blu,bg='#484848',borderwidth=0, activebackground="#484848",command=self.blu1)
        blubu.place(x=235,y=236)
        dblubu = Button(window, image=dblu,bg='#484848',borderwidth=0, activebackground="#484848",command=self.dblu1)
        dblubu.place(x=285,y=236)
        drbu = Button(window, image=dr,bg='#484848',borderwidth=0, activebackground="#484848",command=self.dr1)
        drbu.place(x=335,y=236)
        greenbu = Button(window, image=green,bg='#484848',borderwidth=0, activebackground="#484848",command=self.green1)
        greenbu.place(x=385,y=236)
        greybu = Button(window, image=grey,bg='#484848',borderwidth=0, activebackground="#484848",command=self.grey1)
        greybu.place(x=435,y=236)
        ngbu = Button(window, image=ng,bg='#484848',borderwidth=0, activebackground="#484848",command=self.ng1)
        ngbu.place(x=485,y=236)
        npinkbu = Button(window, image=npink,bg='#484848',borderwidth=0, activebackground="#484848",command=self.npink1)
        npinkbu.place(x=185,y=288)
        obu = Button(window, image=o,bg='#484848',borderwidth=0, activebackground="#484848",command=self.o1)
        obu.place(x=235,y=288)
        pbbu = Button(window, image=pb,bg='#484848',borderwidth=0, activebackground="#484848",command=self.pb1)
        pbbu.place(x=285,y=288)
        pblubu = Button(window, image=pblu,bg='#484848',borderwidth=0, activebackground="#484848",command=self.pblu1)
        pblubu.place(x=335,y=288)
        pgbu = Button(window, image=pg,bg='#484848',borderwidth=0, activebackground="#484848",command=self.pg1)
        pgbu.place(x=385,y=288)
        pinkbu = Button(window, image=pink,bg='#484848',borderwidth=0, activebackground="#484848",command=self.pink1)
        pinkbu.place(x=435,y=288)
        pmbu = Button(window, image=pm,bg='#484848',borderwidth=0, activebackground="#484848",command=self.pm1)
        pmbu.place(x=485,y=288)
        ppbu = Button(window, image=pp,bg='#484848',borderwidth=0, activebackground="#484848",command=self.pp1)
        ppbu.place(x=185,y=340)
        purbu = Button(window, image=pur,bg='#484848',borderwidth=0, activebackground="#484848",command=self.pur1)
        purbu.place(x=235,y=340)
        pybu = Button(window, image=py,bg='#484848',borderwidth=0, activebackground="#484848",command=self.py1)
        pybu.place(x=285,y=340)
        rbu = Button(window, image=r,bg='#484848',borderwidth=0, activebackground="#484848",command=self.r1)
        rbu.place(x=335,y=340)
        turqbu = Button(window, image=turq,bg='#484848',borderwidth=0, activebackground="#484848",command=self.turq1)
        turqbu.place(x=385,y=340)
        wbu = Button(window, image=w,bg='#484848',borderwidth=0, activebackground="#484848",command=self.w1)
        wbu.place(x=435,y=340)
        ybu = Button(window, image=y,bg='#484848',borderwidth=0, activebackground="#484848",command=self.y1)
        ybu.place(x=485,y=340)

    def webhookspamndeletemain(self):
        bkkk = Label(window, image=bacg, borderwidth=0)
        bkkk.place(x=0,y=0)
        self.dadvwebhook = Entry(window,text='a',font=('SeoulHangang',10),bg='#A7A7A7', fg='#000000',width=46,borderwidth=0,show='*')
        self.dadvwebhook.place(x=214, y=138)
        self.dadvcontent = Entry(window,text='b',font=('SeoulHangang',10),bg='#A7A7A7', fg='#000000',width=46,borderwidth=0)
        self.dadvcontent.place(x=214, y=173)
        self.dadvamount = Entry(window,text='c',font=('SeoulHangang',10),bg='#A7A7A7', fg='#000000',width=5,borderwidth=0)
        self.dadvamount.place(x=214, y=209)
        self.dadvusername = Entry(window,text='d',font=('SeoulHangang',10),bg='#A7A7A7', fg='#000000',width=19,borderwidth=0)
        self.dadvusername.place(x=192, y=290)
        self.dadvavatarurl = Entry(window,text='e',font=('SeoulHangang',10),bg='#A7A7A7', fg='#000000',width=19,borderwidth=0)
        self.dadvavatarurl.place(x=192, y=321)
        self.dadvtitle = Entry(window,text='f',font=('SeoulHangang',10),bg='#A7A7A7', fg='#000000',width=19,borderwidth=0)
        self.dadvtitle.place(x=192, y=352)
        self.dadvdesc = Entry(window,text='g',font=('SeoulHangang',10),bg='#A7A7A7', fg='#000000',width=19,borderwidth=0)
        self.dadvdesc.place(x=192, y=383)
        self.dadvauthor = Entry(window,text='h',font=('SeoulHangang',10),bg='#A7A7A7', fg='#000000',width=19,borderwidth=0)
        self.dadvauthor.place(x=459, y=321)
        self.dadvfooter = Entry(window,text='i',font=('SeoulHangang',10),bg='#A7A7A7', fg='#000000',width=19,borderwidth=0)
        self.dadvfooter.place(x=459, y=352)
        self.dadvgif = Entry(window,text='j',font=('SeoulHangang',10),bg='#A7A7A7', fg='#000000',width=19,borderwidth=0)
        self.dadvgif.place(x=459, y=383)
        choosecolor = Button(window, image=choosebu,bg='#363636',borderwidth=0, activebackground="#363636",command=self.colormain)
        choosecolor.place(x=468,y=278)
        if self.delwbhison == False:
            self.delewbh = Button(window, image=blankbu,bg='#363636',borderwidth=0, activebackground="#363636",command=self.delwbhon)
            self.delewbh.place(x=262,y=434)
        else:
            self.delewbh = Button(window, image=fullbu,bg='#363636',borderwidth=0, activebackground="#363636",command=self.delwbhon)
            self.delewbh.place(x=262,y=434)
        if self.hideconon == False:
            self.hidecon = Button(window, image=blankbu,bg='#363636',borderwidth=0, activebackground="#363636",command=self.hidd)
            self.hidecon.place(x=522,y=434)
        else:
            self.hidecon = Button(window, image=fullbu,bg='#363636',borderwidth=0, activebackground="#363636",command=self.hidd)
            self.hidecon.place(x=522,y=434)
        starty = Button(window, image=startbu,bg='#363636',borderwidth=0, activebackground="#363636",command=self.dadvverification)
        starty.place(x=325,y=475)
        
ghosthook()
window.mainloop()