import weather
import json
import webapp2
import datetime 
from google.appengine.ext import db

class Event ( db.Model ):
	event_id = db.StringProperty()
	#create_date = db.DateProperty()
	#expired_date = db.DateProperty()
	#sport_id = db.StringProperty()
	#stadium_id = db.StringProperty()
	#owner_id = db.StringProperty()

class CreateEventPage(webapp2.RequestHandler):
	def get(self, event_id_):
		event = Event( event_id = str(event_id_) )
		text = event.put()
		self.response.headers['Content-Type'] = 'text/plain'
		self.response.write(text)

app = webapp2.WSGIApplication([
	('/api/event/create/(\d+)', CreateEventPage)],debug=True)