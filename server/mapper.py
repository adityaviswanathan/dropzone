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
	result_drops = []	
	for drop in drops:
		result_dict = {}
		for property in Drop.__table__.columns:			
			result_dict[str(property.key)] = getattr(drop, str(property.key))
		user = User.query_by_user_id(result_dict['user_id'])
		if user is not None:
			result_dict['name'] = user.name
			result_dict['photo'] = user.photo
		result_drops.append(result_dict)
	return { 'drops' : result_drops }

def dict_to_drop(payload, drop):
	for property in Drop.__table__.columns:
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