import json
from server.models import *

def user_to_dict(user):
	if user:
		result_dict = {}
		for property in User.__table__.columns:
			result_dict[str(property.key)] = getattr(user, str(property.key))
		return { 'user' : result_dict }
	return {}	

def dict_to_user(payload, user):
	for property in User.__table__.columns:
		if str(property.key) != 'id':
			str(property.key) in payload and setattr(user, str(property.key), payload[str(property.key)])

def drop_to_dict(drop):
	if drop:
		result_dict = {}
		for property in Drop.__table__.columns:
			result_dict[str(property.key)] = getattr(drop, str(property.key))
		return { 'drop' : result_dict }
	return {}

def drops_to_dict(drops):	
	if drops:	
		result_drops = []	
		for drop in drops:
			for property in Drop.__table__.columns:
				result_dict = {}
				result_dict[str(property.key)] = getattr(drop, str(property.key))
			result_drops.append(result_dict)
		return { 'drops' : result_drops }
	return {}

def dict_to_drop(payload, drop):
	for property in Drop.__table__.columns:
		# if str(property.key) == 'location':
		# 	# pass
		# 	drop.set_location(payload['lat'], payload['lng'])
		if str(property.key) != 'id':
			str(property.key) in payload and setattr(drop, str(property.key), payload[str(property.key)])


def pickup_to_dict(pickup):
	if pickup:
		result_dict = {}
		for property in Pickup.__table__.columns:
			result_dict[str(property.key)] = getattr(pickup, str(property.key))
		return { 'pickup' : result_dict }
	return {}

def dict_to_pickup(payload, pickup):
	for property in Pickup.__table__.columns:
		if str(property.key) != 'id':
			str(property.key) in payload and setattr(pickup, str(property.key), payload[str(property.key)])