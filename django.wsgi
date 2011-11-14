import os
import sys

# update this variable to point to your edison installation
#
# EXAMPLE:
# 
# if your site is in /var/djangosites/edison then this needs to be set to '/var/djangosites/'
edisonhome = '/var/djangosites/edison/'


sys.path.append(edisonhome)

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
