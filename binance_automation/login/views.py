from binance_automation import init_firebase_admin
from firebase_admin import auth, exceptions, datetime
from flask import Blueprint, render_template, request, redirect, jsonify, abort

login_bp = Blueprint('login', __name__)


@login_bp.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    
    elif request.method == 'POST':
        idToken = request.json['idToken']
        expires_in = datetime.timedelta(days=1)

        try:
            session_cookie = auth.create_session_cookie(
                idToken, expires_in=expires_in)
            response = jsonify({'status': 'success'})
            expires = datetime.datetime.now() + expires_in
            response.set_cookie(
                'session', session_cookie, expires=expires, httponly=True)  # Add secure=True when deploying
            return response
        except exceptions.FirebaseError:
            return abort(401, 'Failed to create a session cookie')
