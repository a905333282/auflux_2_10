# -*- coding: utf-8 -*-
import time
import application.models as Models
from flask import Blueprint, request, jsonify, current_app, redirect, render_template
from flask_login import current_user, login_user, logout_user, \
    login_required
import application.services.json_tmpl as Json
from flask_babel import gettext as _


auth = Blueprint('auth', __name__, url_prefix='/api/auth')


@auth.route('/user_info', methods=['GET'])
def user_info():
    if not current_user.is_authenticated:
        return jsonify(message='Failed', logged_in=False)

    info = Json.get_user_info(current_user)
    return jsonify(message='OK', logged_in=True, user=info)


@auth.route('/logout', methods=['GET'])
def logout():
    if current_user.is_authenticated:
        logout_user()
    return jsonify(message='OK')


@auth.route('/login_email', methods=['POST'])
def login_email():
    data = request.json
    email = data.get('email', '')
    user, authenticated = Models.User.authenticate(
        email=email, password=data.get('password', ''))
    if not authenticated:
        return jsonify(message='Failed')
    login_user(user, remember=True)
    return jsonify(message='OK', user=Json.get_user_info(user),
                   remember_token=user.generate_auth_token())


@auth.route('/login_with_token', methods=['POST'])
def login_with_token():
    data = request.json
    token = data.get('token', '')
    user = Models.User.verify_auth_token(token)
    if not user:
        return jsonify(message='Failed')
    login_user(user, remember=True)
    return jsonify(message='OK', user=Json.get_user_info(user),
                   remember_token=user.generate_auth_token())


@auth.route('/signup', methods=['POST'])
def email_signup():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    name = data.get('name')
    if not password:
        # 不能为空
        return jsonify(message='Failed', error=_(u'Please fill in.'))

    if Models.User.objects(account__email=email):
        return jsonify(message='Failed', error=_(u'This email has been registered.'))

    if not name:
        name = 'Maybi' + str(time.time()).replace('.','')
    user = Models.User.create(email=email, password=password, name=name)

    login_user(user, remember=True)
    return jsonify(message='OK', user=Json.get_user_info(user),
                   remember_token=user.generate_auth_token())