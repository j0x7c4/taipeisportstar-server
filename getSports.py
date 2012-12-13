import weather
import json
import webapp2

class Sport:
	def __init__ (self):
		self.sports =  json.loads(open('sports.txt').read())

	def get_all_sports (self):
		return self.sports

	def get_sports_by_type (self,type):
		return self.sports

class SportPage(webapp2.RequestHandler):
	def get(self):
		sport = Sport()
		self.response.headers['Content-Type'] = 'text/plain'
		text = json.dumps(sport.get_all_sports(),sort_keys=True)
		self.response.write(text)

app = webapp2.WSGIApplication([('/api/sports/all', SportPage)],debug=True)


if __name__ == '__main__':
	sport = Sport()