import datetime
import sport_model
import stadium_model
from google.appengine.ext import db

class Profile (db.Model):
	fb_user_id = db.StringProperty()
	pop_value = db.FloatProperty()

	def get_profile_by_id ( self, id ):
		profiles = []
		q = db.GqlQuery("SELECT * FROM Profile WHERE fb_user_id = '"+id+"'")
		for item in q:
			profiles.append({u'fb_user_id': item.fb_user_id,
						   u'pop_value': item.pop_value})
		return profiles;

	def get_all_profiles ( self ):
		profiles = []
		q = db.GqlQuery("SELECT * FROM Profile")
		for item in q:
			profiles.append({u'fb_user_id': item.fb_user_id,
						   u'pop_value': item.pop_value})
		return profiles;

