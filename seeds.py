# from server.api import *
from server.models import *
from server import mapper

data = {
	'name':'Sam',
	'email':'sredmond@stanford.edu',
	'photo':''
}
u1 = User()
mapper.dict_to_user(data, u1)

data = {
	'name':'Eddie',
	'email':'eddiew@stanford.edu',
	'photo':''
}
u2 = User()
mapper.dict_to_user(data, u2)

# u1.save()
# u2.save()
# db.session.commit()
print mapper.user_to_dict(u1)
print mapper.user_to_dict(u2)

data = {
	'data_type': 'text',
	'data_payload': 'some words here',
	'numviews': 10,
	'restrictions': 'public',
	'viewcap': 25,
	'user_id': 1,
	'teaser': 'some teaser here',
	'lat': 138.9,
	'lng': 38
}
d = Drop()
mapper.dict_to_drop(data, d)

d.save()
db.session.commit()

print mapper.drop_to_dict(d)

print u1.get_nearby_drops(138.50012, 37.495)