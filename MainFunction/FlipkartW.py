from bs4 import BeautifulSoup
import requests

import getdata
#from fuzzywuzzy import process
def getFlipKartData(text):

#SearchText=input("Enter the Item you want to buy - ")
    
    SearchText=text
    ST=SearchText
   
    page_link = 'https://www.flipkart.com/search?q=XXXX'
    page_link=page_link.replace("XXXX",SearchText)
    print(page_link)
    page_response = requests.get(page_link, timeout=10)
    soup = BeautifulSoup(page_response.content, "html.parser")
    m=soup.find_all("div",{"class":"_3wU53n"})
    n=soup.find_all("div",{"class":"_1vC4OE _2rQ-NK"})
    
    length = len(m)
    
    if (length==0):
         m=soup.find_all("a",{"class":"_2cLu-l"})
         n=soup.find_all("div",{"class":"_1vC4OE"})
    length = len(m)
         
    if (length == 0):
             m=soup.find_all("a",{"class":"_2mylT6"})
             n=soup.find_all("div",{"class":"_1vC4OE"})
    length = len(m)
    if (length == 0):     
            m=soup.find_all("a",{"class":"_2LFGJH"})
            n=soup.find_all("div",{"class":"_1vC4OE"})

    
    print(len(m))
    name,price = getdata.getdatavalue(m,n,ST)
    return(name,price)

"""
name , price = getFlipKartData("Iphone6s Space Gray")

price = price[1:len(price)]
print(price)
price = price.replace(',','')
print(int(price))#"""
    
