from bs4 import BeautifulSoup as bs
from urllib.request import urlopen 



#Web crawler for google news tab in search for most recent articles 

# client = urlopen(URL)

# xmlPage = client.read()

# client.close()


# soupy = bs(xmlPage, "xml")


# newsList = soupy.findAll("item") 

# print("finding news")
# for news in newsList:
# 	print(news.title.text)
# 	print(news.link.text)


##System workflow 

# for loop 
#1. parse all given articles about a specific cryptocurrency in the past X hours 
	#Test for valid sentences and make sure just actual article data is being parsed
	#Hold each sentence in string array || write to jSON file ie mangage the data

# for loop

#2. run vader sentimtent analysis upon each sentece in an artice
#3. Average the article's sentiment based upon all the sentences sentiment
#4 Average all the article's sentiment to generalize a sentiment score 