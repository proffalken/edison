# This file is part of the Edison Project.
# Please refer to the LICENSE document that was supplied with this software for information on how it can be used.
# Create your views here.
from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.forms import ModelForm
from models import *

# Project specific imports
from models import *
def custom_proc(request):
    "A context processor that provides 'app', 'user' and 'ip_address'."
    return {
        'app': 'edison',
        'user': request.user,
        'ip_address': request.META['REMOTE_ADDR']
    }


@login_required
def home(request):
    title = 'Configuration Database Home'
    section_item_name = 'Configuration Item'
    return render_to_response('cmdb/home.tpl',
            locals(),
            context_instance=RequestContext(request, processors=[custom_proc]))

@login_required
def listdata(request):
    link_desc = 'Configuration Item'
    cfgitems = ConfigurationItem.objects.all().order_by('Hostname')
    return render_to_response('list.tpl',{'data_list':cfgitems,'link_desc':link_desc,},context_instance=RequestContext(request)) #{'data_list':cfgitems,locals()})


# Setup the 'edit' form
class EditForm(ModelForm):
    class Meta:
        model = ConfigurationItem

@login_required
def edit(request,cfgid):
    title = 'Edit an Item'
    if request.method == "POST":
        cfgitem = ConfigurationItem.objects.get(pk=cfgid)
        form = EditForm(request.POST,instance=cfgitem)
        if form.is_valid():
           form.save()
           request.user.message_set.create(message='The Configuration Item was updated sucessfully')
           
    else:
        cfgitem = ConfigurationItem.objects.get(pk=cfgid)
        form = EditForm(instance=cfgitem)
    return render_to_response('cmdb/edit.tpl',{'form':form},context_instance=RequestContext(request, processors=[custom_proc]))

@login_required
def add(request):
    title = 'Add a new Item'
    return render_to_response('cmdb/add.tpl',{'form':form},context_instance=RequestContent(request, processors=[custom_proc]))
