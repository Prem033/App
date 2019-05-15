from bs4 import BeautifulSoup
import requests

def getArgosdata():

# Here, we're just importing both Beautiful Soup and the Requests library
    page_link = 'https://www.argos.co.uk/search/iphone 6s/'
# this is the url that we've already determined is safe and legal to scrape from.
    page_response = requests.get(page_link, timeout=10)
# here, we fetch the content from the url, using the requests library
    soup = BeautifulSoup(page_response.content, "html.parser")
#we use the html parser to parse the url content and store it in a variable.
#print('Title=',page_content.title.string)
#print('Price=',page_content.price)
#print(page_content.price)

#print('Price=',page_content.prettify())
#print(page_content.prettify())


    l=soup.find_all("a",{"class":"ac-product-link ac-product-card__details"})


#for i in l:
  #  print(i.text)
   # print(l[0].text)

    return l[0].text



