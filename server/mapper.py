import json
from server.models import *

# user mappings

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