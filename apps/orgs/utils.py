# -*- coding: utf-8 -*-
#

from functools import partial

from common.utils import LocalProxy
from .models import Organization

try:
    from threading import local
except ImportError:
    from django.utils._threading_local import local

_thread_locals = local()


def get_org_from_request(request):
    oid = request.session.get("oid")
    org = Organization.get_instance(oid)
    return org


def set_current_org(org):
    setattr(_thread_locals, 'current_org', org)


def set_to_default_org():
    set_current_org(Organization.default())


def set_to_root_org():
    set_current_org(Organization.root())


def _find(attr):
    return getattr(_thread_locals, attr, None)


def get_current_org():
    return _find('current_org')


current_org = LocalProxy(partial(_find, 'current_org'))
current_user = LocalProxy(partial(_find, 'current_user'))
current_request = LocalProxy(partial(_find, 'current_request'))