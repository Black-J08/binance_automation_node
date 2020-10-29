from binance_automation import init_firebase_admin
from firebase_admin import auth
from flask import Blueprint, request, redirect

index_bp = Blueprint('index', __name__)


@index_bp.route('/')
def index():
    session_cookie = request.cookies.get('session')
    if not session_cookie:
        return redirect('/login')
    try:
        auth.verify_session_cookie(session_cookie, check_revoked=True)
        return 'Index Page'
    except auth.InvalidSessionCookieError:
        return redirect('/login')
