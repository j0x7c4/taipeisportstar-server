import weather
import json
import webapp2
import datetime 
from google.appengine.ext import db

class Event ( db.Model ):
	event_id = db.StringProperty()

	#return a list containing all events
	def get_all_evnets(self):
		events = []
		q = self.all()
		for item in q:
			event = {u'id':item.event_id}
			events.append(event)
		return events

class CreateEventPage(webapp2.RequestHandler):
	def get(self, event_id_):
		event = Event( event_id = str(event_id_) )
		text = event.put()
		self.response.headers['Content-Type'] = 'text/plain'
		self.response.write(text)

class SelectAllEventsPage(webapp2.RequestHandler):
	def get(self):
		event = Event()
		text = json.dumps(event.get_all_evnets(),sort_keys=True)
		self.response.headers['Content-Type'] = 'text/plain'
		self.response.write(text)

app = webapp2.WSGIApplication([
	('/api/event/create/(\d+)', CreateEventPage),
	('/api/event/select/all', SelectAllEventsPage)],debug=True)