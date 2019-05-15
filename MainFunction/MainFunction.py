#import ArgosW
import FlipkartW
#import SnapdealW
import AmazonW
#from fuzzywuzzy import fuzz
#from fuzzywuzzy import process


def mainFunction(SearchText,ProductPrice):

    #SearchText=input("Enter the Item you want to buy - ")
    #ArgosDescription,ArgosPrice = ArgosW.getArgosdata()
    ProductPrice=ProductPrice.replace(',','')
    Price = int(ProductPrice)
    FlipkartDescription,FlipkartPrice = FlipkartW.getFlipKartData(SearchText)
    #SnapdealDescription,SnapdealPrice = SnapdealW.getSnapDealData()
    AmazonDescription,AmazonPrice = AmazonW.getAmazonData(SearchText)
    
    
    print("FlipkartPrice = "+FlipkartPrice)
    print("AmazonPrice =  "+ AmazonPrice)
    
    FlipkartPrice = FlipkartPrice.replace(',','')#Remove ',' character in price
    FlipkartPrice = FlipkartPrice[1:len(FlipkartPrice)]
    AmazonPrice = AmazonPrice.replace(',','')#Remove ',' character in price
    
    FPrice = int(FlipkartPrice) #remove price unit befor converting
    APrice = int(AmazonPrice)
    
    if (FPrice<Price):
        FlipkartPrice="-"
        
    if(APrice<Price):
        AmazonPrice ="-"
        
        
    
    
    
    
    print("<============================================================>\n\n")
    #print("****Data from ARGOS****\n" +ArgosDescription,ArgosPrice+"\n")
    print("****Data from FLIPKART****\n" +FlipkartDescription,FlipkartPrice+"\n")
    #print("****Data from SNAPDEAL****\n" +SnapdealDescription,SnapdealPrice+"\n")
    print("****Data from AMAZON****\n" + AmazonDescription,AmazonPrice+"\n")
    
    return(FlipkartDescription,FlipkartPrice, AmazonDescription,AmazonPrice)



