# This file is part of the Edison Project.
# Please refer to the LICENSE document that was supplied with this software for information on how it can be used.
from greplin import scales
from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.db.models import Q

STATS = scales.collection('/',scales.IntStat('errors'), scales.IntStat('success'))


# Project specific imports
from cmdb.models import *

#
def custom_proc(request):
    "A context processor that provides 'app', 'user' and 'ip_address'."
    return {
        'app': 'Edison',
        'user': request.user,
        'ip_address': request.META['REMOTE_ADDR']
    }

@login_required
def home(request):
	title = 'Edison Home'
	STATS.success += 1
	return render_to_response('home.tpl',
                             locals(),
                             context_instance=RequestContext(request, processors=[custom_proc]))
