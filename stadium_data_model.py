from google.appengine.ext import db
import sport_model


class Stadium ( db.Model ):
	stadium_id = db.IntegerProperty()
	stadium_address = db.StringProperty()
	stadium_lat = db.FloatProperty()
	stadium_long = db.FloatProperty()
	stadium_bus = db.StringProperty()
	stadium_mrt = db.StringProperty()
	stadium_name = db.StringProperty()
	stadium_time = db.StringProperty()
	stadium_type = db.IntegerProperty()
	stadium_sport = db.StringProperty()
	stadium_pop_value = db.FloatProperty()

	def sport_id (s):
		return s[u'id']
	
	def get_sport_list ( sport_id_str ):
		sport_set = sport_model.Sport()
		sports = sorted(sport_set.get_all_sports(),key=sport_id)
		sport_list = []
			sport_id_list = item.stadium_sport.split(',')
			for sport_id in sport_id_list:
				sport_list.append(sports[int(sport_id)])
		return sport_list

	def get_stadiums_by_query ( q ):
		stadiums = []
		for item in q:
			stadium = {u'id':item.stadium_id,
					   u'address':item.stadium_address,
					   u'lat':item.stadium_lat,
					   u'long':item.stadium_long,
					   u'bus':item.stadium_bus,
					   u'mrt':item.stadium_mrt,
					   u'time':item.stadium_time,
					   u'name':item.stadium_name,
					   u'type':item.stadium_type,
					   u'sport':get_sport_list(item.stadium_sport),
					   u'pop_value':item.stadium_pop_value
					   }
			stadiums.append(stadium)
		return stadiums

	def get_all_stadiums(self):
		q = self.all()
		return get_stadiums_by_query(q)

	def get_stadium_by_id(self, stadium_id ):
		q = db.GqlQuery("SELECT * FROM Stadium WHERE stadium_id = "+stadium_id) 
		stadiums = []
		for item in q:
			sport_list = get_sport_list(item.stadium_sport)
			for sport in sport_list:
				if sport[u'name'] == sport_name.decode('utf-8','ignore'):
					stadium = {u'id':item.stadium_id,
							   u'address':item.stadium_address,
							   u'lat':item.stadium_lat,
							   u'long':item.stadium_long,
							   u'bus':item.stadium_bus,
							   u'mrt':item.stadium_mrt,
							   u'time':item.stadium_time,
							   u'name':item.stadium_name,
							   u'type':item.stadium_type,
							   u'sport':sport_list,
							   u'pop_value':item.stadium_pop_value
							   }
					stadiums.append(stadium)
		return stadiums

	def get_stadiums_by_sport ( self, sport_name ):
		q = self.all()
		temp_stadiums =  get_stadiums_by_query(q)
		stadiums = []
		for stadium in temp_stadiums

	def get_stadiums_by_type( self, stadium_type):
		q = db.GqlQuery("SELECT * FROM Stadium WHERE stadium_type = "+stadium_type) 
		return get_stadiums_by_query(q)
