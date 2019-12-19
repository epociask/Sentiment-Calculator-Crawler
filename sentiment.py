from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer



class sentiment:


	def __init__(self):

		self.intensityAnalyzer = SentimentIntensityAnalyzer() #Instantiation 



	def calculateVariedSentiment(sentence):

		#returns collection of polarity scores for given sentence
		return self.intensityAnalyzer.polarity_scores(sentence)




	def getCompoundedSentiment(sentence):

		return calculateVariedSentiment(sentence)



	


