from bs4 import BeautifulSoup
import requests

def getSnapDealData():
# Here, we're just importing both Beautiful Soup and the Requests library


    page_link = 'https://www.snapdeal.com/search?keyword=iphone 6'
# this is the url that we've already determined is safe and legal to scrape from.
    page_response = requests.get(page_link, timeout=10)
# here, we fetch the content from the url, using the requests library
    soup = BeautifulSoup(page_response.content, "html.parser")
#we use the html parser to parse the url content and store it in a variable.

#Below line will get all the class containing Name of the product
#l=soup.find_all("div",{"class":"_3BTv9X"})
    l=soup.find_all("p",{"class":"product-title"})
    m=soup.find_all("span",{"class":"lfloat product-desc-price strike "})
#n=soup.find_all("div",{"class":"_1vC4OE _2rQ-NK"})

#print(l)

    
    for i in l:
        return (l[0].text, m[0].text)
        
        
