

name = db.Column(db.Text)
email = db.Column(db.Text)
photo = db.Column(db.Text)

payload = {
	'name': 'Sam',
	'email': 'foo@stanford.edu',
	'photo': 'some_url'
}
sam = User.create_native(payload)

payload = {
	'name': 'Eddie',
	'email': 'bar@stanford.edu',
	'photo': 'other_url'
}
eddie = User.create_native(payload)

payload = {
	'name': 'Adi',
	'email': 'baz@stanford.edu',
	'photo': 'final_url'
}
adi = User.create_native(payload)

payload = {
	
}
text_drop = Drop.create_native(payload)

payload = {
	
}
image_drop = Drop.create_native(payload)

sam.save()
eddie.save()
adi.save()
text_drop.save()
image_drop.save()

db.session.commit()