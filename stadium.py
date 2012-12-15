# coding=utf-8
import weather
import json
import webapp2
import codecs

class Stadium:
	def __init__ (self):
		self.stadiums = json.loads(open('stadiums.txt').read())
	
	def get_all_stadiums(self):
		return self.stadiums

	def get_stadiums_by_type ( self, type_id ):
		stadiums=[]
		for stadium in self.stadiums:
			if stadium[u'type'] == type_id :
				stadiums.append(stadium)
		return stadiums

	def get_stadiums_by_sport ( self, sport_name ):
		stadiums=[]
		for stadium in self.stadiums:
			sports = stadium[u'sport']
			count = int(stadium[u'count'])
			for idx in range(0,count):
				if sports[str(idx)] == sport_name.decode('utf-8','ignore'):
					stadiums.append(stadium)
					break;
		return stadiums

class AllStadiumPage(webapp2.RequestHandler):
	def get(self):
		stadium = Stadium()
		self.response.headers['Content-Type'] = 'text/plain'
		text = json.dumps(stadium.get_all_stadiums(),sort_keys=True)
		self.response.write(text)

class StadiumByTypePage(webapp2.RequestHandler):
	def get(self,type_id):
		stadium = Stadium()
		self.response.headers['Content-Type'] = 'text/plain'
		text = json.dumps(stadium.get_stadiums_by_type(int(type_id)),sort_keys=True)
		self.response.write(text)

class StadiumBySportPage(webapp2.RequestHandler):
	def get(self,sport):
		stadium = Stadium()
		self.response.headers['Content-Type'] = 'text/plain'
		text = json.dumps(stadium.get_stadiums_by_sport(sport),sort_keys=True)
		self.response.write(text)

app = webapp2.WSGIApplication([
	('/api/stadiums/all', AllStadiumPage),
	('/api/stadiums/type/(\d+)',StadiumByTypePage),
	('/api/stadiums/sport/(.+)',StadiumBySportPage)
	],debug=True)


if __name__ == '__main__':
	stadium = Stadium()
