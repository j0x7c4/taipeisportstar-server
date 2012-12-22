import datetime
import sport_model
import stadium_model
from google.appengine.ext import db

class Event ( db.Model ):
	event_id = db.StringProperty()
	sport_id = db.StringProperty()
	stadium_id = db.StringProperty()
	owner_id = db.StringProperty()
	#return a list containing all events
	def get_all_evnets(self):
		events = []
		q = self.all()
		for item in q:
			event = {u'event_id':item.event_id, u'sport_id':item.sport_id, u'stadium_id':item.stadium_id, u'owner_id':item.owner_id}
			events.append(event)
		return events

	def get_stadium_with_event (self):
		result = []
		stadium_set = stadium_model.Stadium()
		sport_set = sport_model.Sport()
		q = db.GqlQuery("SELECT DISTINCT stadium_id FROM Event")
		for item in q:
			stadium = stadium_set.get_stadium_by_id(int(item.stadium_id))
			stadium[u'event'] = []
			q2 = db.GqlQuery("SELECT * FROM Event WHERE stadium_id = '" + item.stadium_id + "'")
			for item2 in q2:
				stadium[u'event'].append({u'event_id':item2.event_id,
										  u'event_sport':sport_set.get_sport_by_id(item2.sport_id),
										  u'owner_id':item2.owner_id})
			result.append(stadium)
		return result

	def get_sport_with_event (self):
		result = []
		stadium_set = stadium_model.Stadium()
		sport_set = sport_model.Sport()
		q = db.GqlQuery("SELECT DISTINCT sport_id FROM Event")
		for item in q:
			sport = sport_set.get_sport_by_id(item.sport_id)
			sport[u'event'] = []
			q2 = db.GqlQuery("SELECT * FROM Event WHERE sport_id = '" + item.sport_id + "'")
			for item2 in q2:
				sport[u'event'].append({u'event_id':item2.event_id, u'event_stadium':stadium_set.get_stadium_by_id(int(item2.stadium_id)),u'owner_id':item2.owner_id})
			result.append(sport)
		return result