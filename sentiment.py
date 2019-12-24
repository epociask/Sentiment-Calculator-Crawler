from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

class sentiment:



	def __init__(self):

		self.intensityAnalyzer = SentimentIntensityAnalyzer() #Instantiation 


	def calculateVariedSentiment(self, sentence):

		#returns collection of polarity scores for given sentence
		return self.intensityAnalyzer.polarity_scores(sentence)




	def getCompoundedSentiment(self, sentenceList):


		scores = []
		for sentence in sentenceList:
			scores.append(self.calculateVariedSentiment(sentence)['compound'])
			
		return sum(scores) / len(scores)

	


