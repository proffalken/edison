# This file is part of the Edison Project.
# Please refer to the LICENSE document that was supplied with this software for information on how it can be used.
from django.contrib import admin
from piston.models import Nonce, Consumer, Token

admin.site.register(Nonce)
admin.site.register(Consumer)
admin.site.register(Token)
