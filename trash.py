from tkinter import *
import requests
from bs4 import BeautifulSoup
from PIL import ImageTk, Image
import os
win = Tk()
win.geometry('500x300')
win.title('Smart-Bot')
img = ImageTk.PhotoImage(Image.open("old-books-with-white-background-copy-space_23-2148898330.webp"))
panel = Label(win, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")

l1 = Label(win , text='Best Book Price on different websites',width=40 , padx=6)
l1.place(x=50,y=150)
l2 = Label(win , text='Python reference book=' , padx=4)
l2.place(x=80,y=190)

l2 = Label(win , text='1:Python Data Science Handbook			ISBN=9781491912058' , padx=2)
l2.place(x=80,y=250)

l2 = Label(win , text='2:Fluent Python  					ISBN= 9789352132058' , padx=2)
l2.place(x=80,y=300)

l2 = Label(win , text='3:Core Python Programming			  	ISBN=9789386052308' , padx=2)
l2.place(x=80,y=350)

l2 = Label(win , text='4:Python Programming	  			ISBN=9780199480173' , padx=2)
l2.place(x=80,y=400)

l2 = Label(win , text='5:Python Crash Course  				ISBN=9781593279288' , padx=2)
l2.place(x=80,y=450)

l2 = Label(win , text='6:Let Us Python 					ISBN=9789388511568' , padx=2)
l2.place(x=80,y=500)

l2 = Label(win , text='7:Programming and Problem Solving with Python 		ISBN=9789390113026' , padx=2)
l2.place(x=80,y=550)

l2 = Label(win , text='8:Python for beginners 				ISBN=9781393160939' , padx=2)
l2.place(x=80,y=600)

#win.mainloop()

id = input('Enter Id: ')


def flipkart():
    try:
        resp = requests.get('https://www.flipkart.com/indian-woman/p/itmdwuhbkmgugwjv?pid='+id).content
        jsoup = BeautifulSoup(resp, features="html.parser")
        domain = 'Flipkart'
        price1 = jsoup.find('div', attrs={'class': '_30jeq3 _16Jk6d'}).text
        book1 = jsoup.find('span', attrs={'class': 'B_NuCI'}).text.replace('\xa0\xa0', ' ')
        link1 = 'https://www.flipkart.com/indian-woman/p/itmdwuhbkmgugwjv?pid='+id
        dumy1 =  {'data':[domain, price1, book1, link1]}
        print(dumy1)
    except:
        error_msg = ['Flipkart=Not Available']
        print(error_msg)

# Bookswagon
def bookswagon():
    try:
        #id = data
        resp = requests.get('https://www.bookswagon.com/book/angel-answers-oracle-cards-radleigh/'+id).content
        jsoup = BeautifulSoup(resp, features="html.parser")
        domain = 'Bookswagon'
        price2 = jsoup.find('label', attrs={'id': 'ctl00_phBody_ProductDetail_lblourPrice'}).text
        book2 = jsoup.find('label', attrs={'id': 'ctl00_phBody_ProductDetail_lblTitle'}).text
        link2 = 'https://www.bookswagon.com/book/angel-answers-oracle-cards-radleigh/'+id
        dumy2 = {'data':[domain, price2, book2, link2]}
        print(dumy2)
    except:
        error_msg = ['BookSwagon=Not Available']
        print(error_msg)

# spana
def spana():
    try:
        #id = data
        resp = requests.get('https://www.sapnaonline.com/books/'+id).content
        jsoup = BeautifulSoup(resp, features="html.parser")
        domain = 'SpnaOnline'
        price3 = jsoup.find('div', attrs={'class': 'sc-Axmtr AmountBlock__PriceText-zo5xbl-0 jleiXx'}).text
        book3 = jsoup.find('div', attrs={'class': 'sc-Axmtr ProductImageDetailCard__TitleText-xxaxm9-1 dJMXcH'}).text
        link3 = 'https://www.sapnaonline.com/books/'+id
        dumy3 = {'data':[domain, price3, book3, link3]}
        print(dumy3)
    except:
        error_msg = ['Sapna=Not Available']
        print(error_msg)

# bookchor
def bookchor():
    try:
        #id = data
        resp = requests.get('https://www.bookchor.com/book/'+id).content
        jsoup = BeautifulSoup(resp, features="html.parser")
        domain = 'Bookchor'
        price4 = jsoup.find('span', attrs={'class': 'caption-subject bold uppercase pull-right'}).text.strip()
        book4 = jsoup.find('h1').text
        link4 = 'https://www.bookchor.com/book/'+id
        dumy4 =  {'data':[domain,price4, book4, link4]}
        print(dumy4)
    except:
        error_msg = ['BookChor=Not Available']
        print(error_msg)


def all_():
   data =  [flipkart(),bookswagon(),spana(),bookchor()]
   return data
all_()


win.mainloop()
