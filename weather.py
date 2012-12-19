# coding=utf-8
import json
import webapp2
import codecs
import weather_model

class WeatherPage(webapp2.RequestHandler):
	def get(self):
		weather = weather_model.Weather()
		self.response.headers['Content-Type'] = 'text/plain'
		text = json.dumps(weather.get_weather(),sort_keys=True)
		self.response.write(text)

app = webapp2.WSGIApplication([
	('/api/weather', WeatherPage)
	],debug=True)