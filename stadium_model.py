import weather_model
import json

class Stadium:
	def __init__ (self):
		self.stadiums = json.loads(open('stadiums.txt').read())
	
	def get_all_stadiums(self):
		return self.stadiums

	def get_stadiums_by_type ( self, type_id ):
		stadiums=[]
		for stadium in self.stadiums:
			if stadium[u'type'] == type_id :
				stadiums.append(stadium)
		return stadiums
	def get_stadium_by_id ( self, sid ):
		for stadium in self.stadiums:
			if  stadium[u'id'] == sid:
				return stadium
		return None
	def get_stadiums_by_sport ( self, sport_name ):
		stadiums=[]
		for stadium in self.stadiums:
			sports = stadium[u'sport']
			count = int(stadium[u'count'])
			for idx in range(0,count):
				if sports[str(idx)] == sport_name.decode('utf-8','ignore'):
					stadiums.append(stadium)
					break;
		return stadiums