import weather
import json
import webapp2

class Stadium:
	def __init__ (self):
		self.stadiums = json.loads(open('stadiums.txt').read())
	
	def get_all_stadiums(self):
		return self.stadiums

	def get_stadiums_by_type ( self, type ):
		stadiums=[]
		return self.stadiums

	def get_stadiums_by_sport ( self, sport):
		stadiums=[]
		return self.stadiums

class StadiumPage(webapp2.RequestHandler):
	def get(self):
		stadium = Stadium()
		self.response.headers['Content-Type'] = 'text/plain'
		text = json.dumps(stadium.get_all_stadiums(),sort_keys=True)
		self.response.write(text)

app = webapp2.WSGIApplication([('/api/stadiums/all', StadiumPage)],debug=True)


if __name__ == '__main__':
	stadium = Stadium()
