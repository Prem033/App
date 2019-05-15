import requests
from bs4 import BeautifulSoup
import getdata

def getAmazonData(text):

    SearchText=text
    ST=SearchText
    
    global m
    link = 'https://www.amazon.co.in/s?k=XXXX'
    #link= 'https://www.amazon.in/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=XXXX'
    link=link.replace("XXXX",SearchText)
    print(link)
    with requests.Session() as s:
                s.headers['User-Agent'] = 'Mozilla/5.0 ((Windows 7 Professional; Win64; x64)) AppleWebKit/537.36 (KHTML, like Gecko) Safari/537.36 Chrome/74.0.3729.131 (Official Build) (64-bit)'
                response = s.get(link)
                soup = BeautifulSoup(response.text,"lxml")
                m=soup.find_all("span",{"class":"a-size-medium a-color-base a-text-normal"})
                n=soup.find_all("span",{"class":"a-price-whole"})
                length =len(m)
                
                if (length==0):
                    m=soup.find_all("span",{"class":"a-size-base-plus a-color-base a-text-normal"})
                    n=soup.find_all("span",{"class":"a-price-whole"})
                    
                    
                    
                print(len(m))
                name,price = getdata.getdatavalue(m,n,ST)
                return(name,price)
 


"""
name , price = getAmazonData("Iphone6s Space Gray")

print(len(price))
print(price)
price = price.replace(',','')
print(int(price))"""