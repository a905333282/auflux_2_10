import json
from flask import Blueprint, jsonify, request, Response, current_app
from flask_login import login_required, current_user
from flask_babel import gettext as _
from configs.regions_list import REGION_HIERARCHY
import application.models as Models


manage_items = Blueprint('manage_items', __name__, url_prefix='/api/manage_items')


def is_admin():
    roles = current_user.roles
    if 'ADMIN' in roles:
        return True
    else:
        return False


@manage_items.route('/add_item', methods=['POST'])
def add_item():
    if is_admin():
        data = request.json
        print(data)
        return jsonify(message='OK', is_admin=data)
    else:
        return jsonify(message='False', error='Permission denied')
