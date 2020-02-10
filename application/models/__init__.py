# -*- coding: utf-8 -*-
from .user import *
from .permission import *
from .inventory import *

def all():
    result = []
    models = [user, permission, inventory]
    for m in models:
        result += m.__all__
    return result


__all__ = all()