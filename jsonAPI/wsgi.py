"""
WSGI config for jsonAPI project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
import sys
import site
#site.addsitedir('/root/Envs/jsonInput/lib/python2.7/site-packages')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jsonAPI.settings")

path = 'root/ihiredev/jsonAPI'
if path not in sys.path:
    sys.path.append(path)
    sys.path.append('/root/ihiredev/jsonAPI/jsonAPI')
    sys.path.append('/root/ihiredev')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
