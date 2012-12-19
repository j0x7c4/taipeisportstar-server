import urllib
import json
import math

class Weather:
	def __init__ (self):
		woeid = '2306179'
   		query_url = 'http://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%3D'+woeid+'%20and%20u%3D%22c%22&format=json'
		self.weather_json = json.loads(urllib.urlopen(query_url).read())
		self.rain_prob_json = json.loads(open('rain_prob.txt').read())
	
		results = self.weather_json[u'query'][u'results'][u'channel'];
		condition = results[u'item'][u'condition']

		self.location = results[u'location'][u'city'] + ', ' + results[u'location'][u'country']
		self.condition = {u'text':condition[u'text'], u'temp':condition[u'temp'], u'code':condition[u'code']}
		self.time = results[u'item'][u'pubDate']
		self.image = {u'url':"http://l.yimg.com/a/i/us/we/52/"+condition[u'code']+".gif", u'height':52, u'width':52}

	def get_outdoor_sport_weight (self):
		p = 1
		rain_p = self.rain_prob_json[int(self.condition[u'code'])][u'p']
		d_temp = int(self.condition[u'temp']) - 27
		p = math.exp(-d_temp*d_temp/25)
		return p

	def get_weather (self):
		return {u'location':self.location, u'condition':self.condition, u'time':self.time, u'image':self.image}
		

if __name__ == "__main__":
	weather = Weather()
	print weather.get_outdoor_sport_weight()
	print weather.get_weather()

