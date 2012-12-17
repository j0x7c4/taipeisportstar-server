import datetime
import sport_model
import stadium_model
from google.appengine.ext import db

class Event ( db.Model ):
	event_id = db.StringProperty()
	sport_id = db.StringProperty()
	stadium_id = db.StringProperty()

	#return a list containing all events
	def get_all_evnets(self):
		events = []
		q = self.all()
		for item in q:
			event = {u'event_id':item.event_id, u'sport_id':item.sport_id, u'stadium_id':item.stadium_id}
			events.append(event)
		return events

	def get_stadium_with_event (self):
		events = []
		q = self.all()
		return events

	def get_sport_with_event (self):
		events = []
		return events