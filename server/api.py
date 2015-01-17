from server import mapper
from server.models import *
from flask import render_template, jsonify, request, redirect, url_for, abort
import json

# user API

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