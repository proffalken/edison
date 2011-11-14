# This file is part of the Edison Project.
# Please refer to the LICENSE document that was supplied with this software for information on how it can be used.
from django.shortcuts import render_to_response
from django.template import RequestContext

def request_token_ready(request, token):
    error = request.GET.get('error', '')
    ctx = RequestContext(request, {
        'error' : error,
        'token' : token})
    return render_to_response('api/request_token_ready.html',
                          context_instance = ctx)
