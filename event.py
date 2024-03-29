import json
import webapp2
import datetime 
import event_model

class CreateEventPage(webapp2.RequestHandler):
	def get(self, event_id_ , sport_id_, stadium_id_ , owner_id_ ):
		event = event_model.Event( event_id = str(event_id_), 
								   sport_id = str(sport_id_), 
								   stadium_id = str(stadium_id_),
								   owner_id = str(owner_id_) )
		text = event.put()
		self.response.headers['Content-Type'] = 'text/plain'
		self.response.write(text)

class SelectAllEventsPage(webapp2.RequestHandler):
	def get(self):
		event = event_model.Event()
		text = json.dumps(event.get_all_events(),sort_keys=True)
		self.response.headers['Content-Type'] = 'text/plain'
		self.response.write(text)

class SelectStadiumWithEvent(webapp2.RequestHandler):
	def get(self):
		event = event_model.Event()
		text = json.dumps(event.get_stadium_with_event(),sort_keys=True)
		self.response.headers['Content-Type'] = 'text/plain'
		self.response.write(text)

class SelectSportWithEvent(webapp2.RequestHandler):
	def get(self):
		event = event_model.Event()
		text = json.dumps(event.get_sport_with_event(),sort_keys=True)
		self.response.headers['Content-Type'] = 'text/plain'
		self.response.write(text)
class SelectEventsWithOwnerIdPage(webapp2.RequestHandler):
	def get(self,owner_id):
		event = event_model.Event()
		text = json.dumps(event.get_events_by_owner_id(owner_id),sort_keys=True)
		self.response.headers['Content-Type'] = 'text/plain'
		self.response.write(text)
		
app = webapp2.WSGIApplication([
	('/api/event/create/(\d+)/(\d+)/(\d+)/(\d+)', CreateEventPage),
	('/api/event/select/sport', SelectSportWithEvent),
	('/api/event/select/stadium', SelectStadiumWithEvent),
	('/api/event/select/ownerid/(\d+)', SelectEventsWithOwnerIdPage),
	('/api/event/select/all', SelectAllEventsPage)],debug=True)