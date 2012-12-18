import json
import weather_model

class Sport:
	def __init__ (self):
		self.sports =  json.loads(open('sports.txt').read())

	def get_all_sports (self):
		return self.sports

	def get_sports_by_type (self,type_id):
		sports = []
		for sport in self.sports:
			if sport[u'type'] == type_id:
				sports.append(sport)
		return sports

	def get_sport_by_id (self, sport_id):
		for sport in self.sports:
			if sport[u'id'] == sport_id:
				return sport
		return None

if __name__ == '__main__':
	sport_set = Sport()
	sport = sport_set.get_sport_by_id(0)
	sport[u'aaa'] = []
	print sport