# -*- coding: utf-8 -*-

from .user import *
from .address import *


def all():
    result = []
    models = [user, address]
    for m in models:
        result += m.__all__
    return result


__all__ = all()
