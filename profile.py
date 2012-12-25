import json
import webapp2
import datetime 
import profile_model

class CreateProfilePage(webapp2.RequestHandler):
	def get(self, user_id):
		profile = profile_model.Profile( fb_user_id = str(user_id), pop_value = 1.0)
		text = profile.put()
		self.response.headers['Content-Type'] = 'text/plain'
		self.response.write(text)

class SelectAllProfilesPage(webapp2.RequestHandler):
	def get(self):
		profile = profile_model.Profile()
		text = json.dumps(profile.get_all_profiles(),sort_keys=True)
		self.response.headers['Content-Type'] = 'text/plain'
		self.response.write(text)


class SelectProfileByIDPage(webapp2.RequestHandler):
	def get(self, user_id):
		profile = profile_model.Profile()
		text = json.dumps(profile.get_profile_by_id(user_id),sort_keys=True)
		self.response.headers['Content-Type'] = 'text/plain'
		self.response.write(text)

app = webapp2.WSGIApplication([
	('/api/profile/create/(\d+)', CreateProfilePage),
	('/api/profile/select/all',SelectAllProfilesPage),
	('/api/profile/select/id/(\d+)', SelectProfileByIDPage)],debug=True)