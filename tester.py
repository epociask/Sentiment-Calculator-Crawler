from bs4 import BeautifulSoup as bs
import requests 
import re
from sentiment import *  


def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>') #regex command to clean html
  cleantext = re.sub(cleanr, '', raw_html) 
  cleantext = cleantext.replace(" , ", "") #removes unnecessary commas
  return cleantext[ 1 : len(cleantext) - 1].split(".") #splits sentences into list 


page = requests.get("https://www.coindesk.com/ethereum-network-draws-developer-ire-after-scheduling-new-years-day-upgrade")
temp = bs(page.content, "html.parser")

#print(temp.get_text())
article = cleanhtml(str(temp.find_all(class_="article-pharagraph")))


x = sentiment()

print(x.getCompoundedSentiment(article))


