# coding=utf-8
import json
import webapp2
import codecs
import stadium_model

class AllStadiumPage(webapp2.RequestHandler):
	def get(self):
		stadium = stadium_model.Stadium()
		self.response.headers['Content-Type'] = 'text/plain'
		text = json.dumps(stadium.get_all_stadiums(),sort_keys=True)
		self.response.write(text)

class StadiumByTypePage(webapp2.RequestHandler):
	def get(self,type_id):
		stadium = stadium_model.Stadium()
		self.response.headers['Content-Type'] = 'text/plain'
		text = json.dumps(stadium.get_stadiums_by_type(int(type_id)),sort_keys=True)
		self.response.write(text)

class StadiumByIdPage(webapp2.RequestHandler):
	def get(self,sid):
		stadium = stadium_model.Stadium()
		self.response.headers['Content-Type'] = 'text/plain'
		text = json.dumps(stadium.get_stadium_by_id(int(sid)),sort_keys=True)
		self.response.write(text)

class StadiumBySportPage(webapp2.RequestHandler):
	def get(self,sport):
		stadium = stadium_model.Stadium()
		self.response.headers['Content-Type'] = 'text/plain'
		text = json.dumps(stadium.get_stadiums_by_sport(sport),sort_keys=True)
		self.response.write(text)

app = webapp2.WSGIApplication([
	('/api/stadiums/all', AllStadiumPage),
	('/api/stadiums/type/(\d+)',StadiumByTypePage),
	('/api/stadiums/id/(\d+)',StadiumByIdPage),
	('/api/stadiums/sport/(.+)',StadiumBySportPage)
	],debug=True)