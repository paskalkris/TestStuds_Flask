import datetime
from wtfpeewee.orm import model_form
from flask import g, Blueprint, session, flash
from flask import render_template, redirect, url_for, request
from hashlib import md5
from peewee import IntegrityError

from app.universal import get_object_or_404
from app.init_db import database
from .models import User
from .session import auth_user

bp = Blueprint('acc', __name__, template_folder='templates')

@bp.route('/join/', methods=['GET', 'POST'])
def join():
    if request.method == 'POST' and request.form['username']:
        try:
            with database.db.transaction():
                user = User.create(
                    username=request.form['username'],
                    password=md5((request.form['password']).encode('utf-8')).hexdigest(),
                    join_date = datetime.datetime.now())
            auth_user(user)
            return redirect(url_for('group.groups_list'))
        except IntegrityError:
            flash('Пользователь с таким именем уже существует')
    LoginForm = model_form(User, exclude=('join_date',))
    form = LoginForm()
    return render_template('acc/login.html', form=form)


@bp.route('/login/', methods=['GET', 'POST'])
def login():
    next_url = request.args.get('next') or request.form.get('next')
    LoginForm = model_form(User, exclude=('join_date',))
    form = LoginForm()
    if request.method == 'POST' and request.form['username']:
        try:
            user = User.get(
                username=request.form['username'],
                password=md5((request.form['password']).encode('utf-8')).hexdigest())
        except User.DoesNotExist:
            errors = "Неверное имя пользователя или пароль. Повторите попытку"
            return render_template('acc/login.html', form=form, next=next_url, error_message=errors)
        else:
            auth_user(user)
            return redirect(next_url) # or url_for('group.groups_list'))
    LoginForm = model_form(User, exclude=('join_date',))
    form = LoginForm()
    return render_template('acc/login.html', form=form, next=next_url)


@bp.route('/logout/')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('group.groups_list'))