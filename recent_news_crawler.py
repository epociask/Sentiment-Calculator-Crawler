from bs4 import BeautifulSoup as bs
import requests



#Web crawler for google news tab in search for most recent articles 


class recent_news_crawler:

	def __init__(self):
		self.links = []
		self.htmls = []
	def parseSearchQueryLinks(self, searchQ, month, fromDay, ToDay, year):


		URL = 'https://www.google.com/search?pz=1&cf=all&ned=us&hl=en&tbm=nws&gl=us&as_q='+searchQ+'&as_occt=any&as_drrb=b&as_mindate='+month+'%2F'+fromDay+'%2F'+year+'&as_maxdate='+month+'%2F'+ToDay+'%2F'+year+'&tbs=cdr%3A1%2Ccd_min%3A3%2F1%2F13%2Ccd_max%3A3%2F2%2F13&as_nsrc=Gulf%20Times&authuser=0'
		page = requests.get(URL)

		tempArr = []
		tempArr = str(page.content).split("<")
		#print(page.content)

		for line in tempArr:
			#parses line 
			if(line.find("a href=") != -1 and line.find('google') == -1):
				line = line[15 : len(line)-2]
				self.links.append(line)

	
		


	def convertLinkToHtml(self):

		print(len(self.links))

		for link in self.links:

			try:
				page = requests.get(link)
				soup = bs(page.content, 'html.parser')
				self.htmls.append(soup)
				
		
			except Exception:
				pass

	def getPages(self):

		count = 0 
		for link in self.links:
			#if(link.find("coindesk") != -1):
			print(link)
			++count


temp = recent_news_crawler()
temp.parseSearchQueryLinks("ethereum", "12", "21", "22", "2019")
temp.convertLinkToHtml()
temp.getPages()
temp.parseSearchQueryLinks("bitcoin", "12", "21", "22", "2019")
temp.convertLinkToHtml()
temp.getPages()
#print(tmpe)
##System workflow 

# for loop 
#1. parse all given articles about a specific cryptocurrency in the past X hours 
	#Test for valid sentences and make sure just actual article data is being parsed
	#Hold each sentence in string array || write to jSON file ie mangage the data

# for loop

#2. run vader sentimtent analysis upon each sentece in an artice
#3. Average the article's sentiment based upon all the sentences sentiment
#4 Average all the article's sentiment to generalize a sentiment score 