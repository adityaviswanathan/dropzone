from server import mapper
from server.models import *
from flask import render_template, jsonify, request, redirect, url_for, abort
import json

# user API

@app.route('/api/user/<int:user_id>/nearby', methods=['GET'])
def read_nearby_drops(user_id):
    user = User.query_by_user_id(user_id)
    print "Incoming data:", request.args
    payload = json.loads(request.data)
    if user is None:
        abort(404)
    lat = float(request.args.get('lat'))
    lng = float(request.args.get('lng'))
    if lat is None:
        abort(404)
    if lng is None:
        abort(404)
    drops = User.get_nearby_drops(lat, lng)
    print "Nearby drops: ", drops
    return jsonify(mapper.drops_to_dict(drops))

@app.route('/api/user', methods=['POST'])
def create_user():
    payload = json.loads(request.data)
    print 'THIS IS THE PAYLOAD\n'
    print payload
    user = User.query_by_email(payload['email'])
    if user is None:
        user = User()
    mapper.dict_to_user(payload, user)
    user.save()
    db.session.commit()
    return jsonify(mapper.user_to_dict(user)) 

@app.route('/api/user/<int:user_id>', methods=['GET'])
def read_user(user_id):
    user = User.query_by_user_id(user_id)
    if user is None:
        abort(404)
    return jsonify(mapper.user_to_dict(user))

@app.route('/api/user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
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
    user = User.query_by_user_id(user_id)
    if user is None:
        abort(404)
    user.delete()
    db.session.commit()
    return user_id

@app.route('/api/drop', methods=['POST'])
def create_drop():
    payload = json.loads(request.data)
    drop = Drop()
    mapper.dict_to_drop(payload, drop)
    drop.save()
    db.session.commit()
    return jsonify(mapper.drop_to_dict(drop))

def payment_transfer(user_1, user_2, amount):
    user_1 -= int(amount)
    user_2 += int(amount)
    user_1.save()
    user_2.save()

def consume_drop(user_id, drop):
    if drop.data_type == 'payment':
        payment_transfer(drop.user_id, user_id, drop.data_payload)
    drop.numviews += 1
    pickup = Pickup()
    payload = {
        'user_id' : user_id,
        'drop_id' : drop.id
    }
    mapper.dict_to_pickup(payload, pickup)
    pickup.save()
    drop.save()

@app.route('/api/drop/<int:drop_id>/<int:user_id>', methods=['GET'])
def read_drop(drop_id=None, user_id=None):
    drop = Drop.query_by_drop_id(drop_id)
    if drop is None:
        abort(404)
    if user_id is None:
        abort(404)
    consume_drop(user_id, drop) 
    db.session.commit()
    return jsonify(mapper.drop_to_dict(drop))

@app.route('/api/drop/<int:drop_id>', methods=['PUT'])
def update_drop(drop_id):
    payload = json.loads(request.data)
    drop = Drop.query_by_drop_id(drop_id)
    if drop is None:
        abort(404)
    mapper.dict_to_drop(payload, drop)
    drop.save()
    db.session.commit()
    return jsonify(mapper.drop_to_dict(drop))

@app.route('/api/drop/<int:drop_id>', methods=['DELETE'])
def delete_drop(drop_id):
    drop = Drop.query_by_drop_id(drop_id)
    if drop is None:
        abort(404)
    drop.delete()
    db.session.commit()
    return drop_id

@app.route('/api/pickup', methods=['POST'])
def create_pickup():
    payload = json.loads(request.data)
    pickup = Pickup()
    mapper.dict_to_pickup(payload, pickup)
    pickup.save()
    db.session.commit()
    return jsonify(mapper.pickup_to_dict(pickup))   

@app.route('/api/pickup/<int:pickup_id>', methods=['GET'])
def read_pickup(pickup_id):
    pickup = Pickup.query_by_pickup_id(pickup_id)
    if pickup is None:
        abort(404)
    return jsonify(mapper.pickup_to_dict(pickup))

@app.route('/api/pickup/<int:pickup_id>', methods=['PUT'])
def update_pickup(pickup_id):
    payload = json.loads(request.data)
    pickup = Pickup.query_by_pickup_id(pickup_id)
    if pickup is None:
        abort(404)
    mapper.dict_to_pickup(payload, pickup)
    pickup.save()
    db.session.commit()
    return jsonify(mapper.pickup_to_dict(pickup))

@app.route('/api/pickup/<int:pickup_id>', methods=['DELETE'])
def delete_pickup(pickup_id):
    pickup = Pickup.query_by_pickup_id(pickup_id)
    if pickup is None:
        abort(404)
    pickup.delete()
    db.session.commit()
    return pickup_id
