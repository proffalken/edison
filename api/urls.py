# This file is part of the Edison Project.
# Please refer to the LICENSE document that was supplied with this software for information on how it can be used.
from django.conf.urls.defaults import *
from piston.resource import Resource

from api.handlers import *

cfgitem_resource = Resource(handler=CfgItemHandler)
puppet_resource = Resource(handler=PuppetHandler)
package_resource = Resource(handler=PackageHandler)
libvirt_resource = Resource(handler=LibVirtHandler)
kickstart_resource = Resource(handler=KickstartHandler)

urlpatterns = patterns('',
    #url(r'^kickstart/(?P<hostname>[^/]+)/$', kickstart_resource, {'emitter_format':'raw'}), 
    url(r'^kickstart/', kickstart_resource, {'emitter_format':'raw'}), # Can't close this off at the final "/" because anaconda tries different things... :(
    url(r'^puppet/(?P<hostname>[^/]+)/$', puppet_resource,{'emitter_format':'yaml'}), 
    url(r'^hosts/(?P<hostname>[^/]+)/$', cfgitem_resource), 
    url(r'^libvirt/(?P<hostname>[^/]+)/$', libvirt_resource), 
    url(r'^auditorium/packages$', package_resource),
)

urlpatterns += patterns(
    'piston.authentication',
    url(r'^oauth/request_token/$','oauth_request_token'),
    url(r'^oauth/authorize/$','oauth_user_auth'),
    url(r'^oauth/access_token/$','oauth_access_token'),
)

