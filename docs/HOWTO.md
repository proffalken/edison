# How to use Edison 

*This guide is subject to change as the project progresses, however it aims to act as a general overview on how to install and start using Edison in its present state.*

## Installing

To install Edison you have two choices:

*  mod_wsgi (preferred)
*  Built-in server using mange.py

Please be aware that if you choose to use the build-in server, you will need to update the media paths in settings.py to point to the correct urls.

### Installing using mod_wsgi

1.  Ensure that [mod_wsgi][1] is installed and working under apache
2.  Checkout Edison from github into an appropriate directory (we use /var/djangosites/edison here, so make sure you update any paths accordingly f you're installing somewhere different!)
3.  Copy "edison.apache.conf" from the "contrib" directory into your apache conf.d directory if on Centos/Redhat and into the "sites-available" directory if using Debian/Ubuntu
4.  Edit the edison.apache.conf file so that it matches your paths and host names (by default, it sets up a VirtualHost named "edison" listening on port 80)
5.  If on Centos/RedHat, restart/reload httpd, if running Debian/Ubuntu then run a2ensite for the appropriate site and then reload/restart apache2
6.  Edit settings.py and ensure that you have setup your database correctly
7.  Run "manage.py syncdb" from the main directory of the edison source code and make sure you setup an admin user
8.  Visit the appropriate virtual server in your browser and log in using the admin user you have just created

### Installing using the build-in server

1.  Update settings.py URLS/Paths to match the correct settings for your machine
2.  Run "manage.py syncdb" and ensure you create a default user for the Admin interface
3.  Run "manage.py runserver" and connect to the port advertised on your local host

## Using Edison

### Adding Data

The quickest way to make sure you have all the data you need for a host is to log in to the admin interface (http://edison/admin/ if you're using mod_wsgi with the default configs) and add a new Configuration Item from the CMDB section.

The first time you add a host into Edison it can be quite time consuming owing to the (deliberate) constraints within the models which mean that a host must be assigned to a rack, the rack must be assigned to a room/suite which in turn must be assigned to a datacentre which is run by a company at a give address etc, etc. however the good news is that if all your hosts are in one datacentre, you'll only have to go through this once! ;)

We're hoping to improve the current web interface in the coming months so that it will make this kind of thing less painful, so keep an eye on the code! :)

### Using Edison with Puppet

If you want to use Edison with puppet, you'll need to setup your classes in the "Orchestration" area and assign them to your hosts.

Once you've done this, copy the edison-ext-hosts script from the "contrib" dir somewhere in your path (we tend to use /usr/local/bin/) and configure puppet.conf on your puppetmaster to use this as the external_nodes script as follows:

    external_nodes = /usr/local/bin/edison-ext-nodes
    node_terminus = exec

If you want the ability to use your datacentre/room/rack and any metadata that you create through "Orchestra" to be available as custom facts, just make sure you push the system_setup.rb file from the contrib directory to /var/lib/puppet/lib/facter on your puppet clients.

With both scripts, you'll need to check it is performing a lookup against the correct domain/port.

I'm currenty working on a version of these scripts that use SSL to connect to the server and at some-point this will probably move to either OAuth or SSL Client Certificates to ensure that sensitive data is not revealed durIf you want the ability to use your datacentre/room/rack and any metadata that you create through "Orchestra" to be available as custom facts, just make sure you push the system_setup.rb file from the contrib directory to /var/lib/puppet/lib/facter on your puppet clients.

With both scripts, you'll need to check it is performing a lookup against the correct domain/port.

I'm currently working on a version of these scripts that use SSL to connect to the server and at some-point this will probably move to either OAuth or SSL Client Certificates to ensure that sensitive data is not revealed during transmission.

### Using the API

Currently there are three API urls that work:

*  http://edison/api/puppet/<FQDN of Host>/ - returns metadata and puppet classes
*  http://edison/api/hosts/<FQDN of Host>/ - returns hostname, rack, room, suite, datacentre and class.
*  http://edison/api/kickstart/ - returns the value from the AutoInstallFile field on the Configuration Item Profile when sent the X-RHN-Provisioning-Mac-0 header

All urls are generated using Piston, therefore you can get XML, JSON, Raw Text or YAML out of them simply by appending ?format=xml/json/raw/yaml to the end of the query string. 

e.g·

http://edison/api/hosts/<FQDN of Host>/?format=xml - list the hostname, rack, room, suite, datacentre and configuration item class (server/printer etc) in xml format
http://edison/api/puppet/<FQDN of Host>/?format=yaml - list the puppet classes and metadata in YAML format (the most likely option for puppet and the one used in edison-ext-nodes)

The kickstart output is based upon the value in the ConfigurationItemProfile.AutoInstallFile field.  There is now support for rudimentary templating:

	<<hostname>> is replaced by the value of ConfigurationItem.Hostname for the MacAddress sent
	<<tree>> is replaced by http://<EDISON_SERVER>/cmdb/installtree/<ConfigurationItem.Hostname>/ - this will enable you to configure an install tree based upon the host or profile
	<<rootpw>> is replaced by the value of rootpwhash as set on the configuration item
	<<bootdev>> is replaced by the macaddress used to request the kickstart

[1] http://code.google.com/p/modwsgi/
