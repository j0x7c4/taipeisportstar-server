from google.appengine.ext import db

class Sport( db.Model ): 
	sport_id = db.IntegerProperty()
	sport_type = db.IntegerProperty()
	sport_name = db.StringProperty()
	sport_pop_value = db.FloatProperty()

	def get_all_sports (self):
		sports = []
		q = self.all()
		for item in q:
			sport = {u'id':item.sport_id,
					 u'type':item.sport_type,
					 u'name':item.sport_name,
					 u'pop_value':item.sport_pop_value}
			sports.append(sport)
		return sports

	def get_sports_by_type (self,type_id):
		sports = []
		q = db.GqlQuery("SELECT * FROM Sport WHERE sport_type = "+type_id)
		for item in q:
			sport = {u'id':item.sport_id,
					 u'type':item.sport_type,
					 u'name':item.sport_name,
					 u'pop_value':item.sport_pop_value}
			sports.append(sport)
		return sports

	def get_sport_by_id (self, sport_id):
		q = db.GqlQuery("SELECT * FROM Sport WHERE sport_id = "+sport_id)
		for item in q:
			sport = {u'id':item.sport_id,
					 u'type':item.sport_type,
					 u'name':item.sport_name,
					 u'pop_value':item.sport_pop_value}
			return sport
		return None

