# This file is part of the Edison Project.
# Please refer to the LICENSE document that was supplied with this software for information on how it can be used.
# ensure that we include all the models required to administer this app
from models import *
from django.contrib import admin

admin.site.register(Package)
