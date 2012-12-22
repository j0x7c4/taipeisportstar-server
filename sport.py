import json
import webapp2
import sport_model

class AllSportPage(webapp2.RequestHandler):
	def get(self):
		sport = sport_model.Sport()
		self.response.headers['Content-Type'] = 'text/plain'
		text = json.dumps(sport.get_all_sports(),sort_keys=True)
		self.response.write(text)

class SportByTypePage(webapp2.RequestHandler):
	def get(self, type_id):
		sport = sport_model.Sport()
		self.response.headers['Content-Type'] = 'text/plain'
		text = json.dumps(sport.get_sports_by_type(type_id),sort_keys=True)
		self.response.write(text)

class SportByIdPage(webapp2.RequestHandler):
	def get(self, sport_id):
		sport = sport_model.Sport()
		self.response.headers['Content-Type'] = 'text/plain'
		text = json.dumps(sport.get_sport_by_id(sport_id),sort_keys=True)
		self.response.write(text)

app = webapp2.WSGIApplication([
	('/api/sports/all', AllSportPage),
	('/api/sports/id/(\d+)',SportByIdPage),
	('/api/sports/type/(\d+)',SportByTypePage)],debug=True)