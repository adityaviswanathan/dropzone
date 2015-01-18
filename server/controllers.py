import os
from flask import g, render_template, url_for, flash, redirect, request
from flask.ext.login import login_user, logout_user, current_user, login_required
from server.login import facebook, facebook_dev
from server.models import *
from server import mapper
from pprint import pprint

print "In controllers"

@app.route('/<path:path>')
@app.route('/')
def index(path=None):
    return render_template('index.html', name="dropzone")

@app.route('/facebook/login', methods=['GET'])
def facebook_login():
    redirect_uri = url_for('facebook_authorized', _external=True)
    params = {'redirect_uri': redirect_uri, 'scope': 'email, public_profile'}
    if(os.environ['APP_SETTINGS'] == 'server.config.ProductionConfig'):
        return redirect(facebook.get_authorize_url(**params))
    if(os.environ['APP_SETTINGS'] == 'server.config.DevelopmentConfig'):
        return redirect(facebook_dev.get_authorize_url(**params))

    

@app.route('/facebook/authorized')
def facebook_authorized():
    # check to make sure the user authorized the request
    if not 'code' in request.args:
        flash('You did not authorize the request')
        return redirect(url_for('index'))

    # make a request for the access token credentials using code
    redirect_uri = url_for('facebook_authorized', _external=True)
    data = dict(code=request.args['code'], redirect_uri=redirect_uri)
    session = {}
    if(os.environ['APP_SETTINGS'] == 'server.config.ProductionConfig'):
        session = facebook.get_auth_session(data=data)
    if(os.environ['APP_SETTINGS'] == 'server.config.DevelopmentConfig'):
        session = facebook_dev.get_auth_session(data=data)
    
    me = session.get('me').json()
    pprint(me)
    payload = { 'name' : me['name'],
                'email' : me['email'],
                'photo' : 'https://graph.facebook.com/' + me['id'] + '/picture' }
           
    user = User.query_by_email(payload['email'])
    if user is None:
        user = User()
    mapper.dict_to_user(payload, user)
    user.save()
    db.session.commit()
    # return render_template('index.html', name="shopdrop", id=user.id)
    return redirect(url_for('index')) 