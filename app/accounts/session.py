from flask import session, flash, redirect, url_for, request
from functools import wraps

from .models import User

def auth_user(user):
    session['logged_in'] = True
    session['user_id'] = user.id
    session['username'] = user.username
    flash('Вы вошли под пользователем %s' % (user.username))

def get_current_user():
    if session.get('logget_in'):
        return User.get(User.id == session['user_id'])

def login_required(f):
    @wraps(f)
    def inner(*args, **kwargs):
        if not session.get('logged_in'):
            return redirect(url_for('acc.login', next=request.path))
        return f(*args, **kwargs)
    return inner