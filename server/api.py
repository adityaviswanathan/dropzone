from server import mapper
from server.models import *
from flask import render_template, jsonify, request, redirect, url_for, abort
import json

# user API

@app.route('/api/user/login', methods=['POST'])
def login_user():
	payload = json.loads(request.data)
	user = User.query_by_email(payload['email'])
	if user is None:
		abort(404)
	if user.verify_password(payload['password']):
		return jsonify(mapper.user_to_dict(user))
	abort(401)
	return 'invalid credentials\n' # need to return identifier (id)

# NOT NEEDED IF ONLY FB LOGIN, WILL REMOVE SOON
@app.route('/api/user', methods=['POST'])
def create_user():
	# payload = request.form
	# if(request.type == json):
	# need to return err to client if user exists (based on email)
	# need to associate password with email (if already signed in via fb)?
	
	# BEHAVIOR: returns user found by supplied email or creates and returns new user

	payload = json.loads(request.data)
	user = User.query_by_email(payload['email'])
	if user is None:
		user = User.create_native(payload)
	mapper.dict_to_user(payload, user)
	# user.save()
	# db.session.commit()
	return jsonify(mapper.user_to_dict(user)['user'])

@app.route('/api/user/<int:user_id>', methods=['GET'])
def read_user(user_id):
	user = User.query_by_user_id(user_id)
	if user is None:
		abort(404)
	return jsonify(mapper.user_to_dict(user))

@app.route('/api/user/<int:user_id>', methods=['PUT'])
def update_user(user_id):	
	# payload = request.form
	# if(request.type == json):
	payload = json.loads(request.data)
	user = User.query_by_user_id(user_id)
	if user is None:
		abort(404)
	mapper.dict_to_user(payload, user)
	user.save()
	db.session.commit()
	return jsonify(mapper.user_to_dict(user))

@app.route('/api/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
	# payload = request.form
	# if(request.type == json):
	# payload = json.loads(request.data)
	user = User.query_by_user_id(user_id)
	if user is None:
		abort(404)
	user.delete()
	db.session.commit()
	return 'user deleted\n'

@app.route('/api/drop/<int:drop_id>', methods=['GET']):
def get_drop(drop_id):
	drop = Drop.query_by_drop_id(drop_id)
	if drop is None:
		abort(404)
	return jsonify(mapper.drop_to_dict(drop))