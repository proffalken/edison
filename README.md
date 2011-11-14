# Edison 

"The Hamster that keeps your infrastructure running..."

## What is Edison? 

Edison is a Django-based framework for Change Management, Automated or Unattended installs, Configuration Management and just about anything else to do with your IT infrastructure that you want to build a new App for.

## Why should I use Edison instead of 'x' that already exists? 

A good question. A the moment, you shouldn't.

This project is very young and even the developers aren't running it in a production environment at the moment (although we are seeing some sucess with Puppet Integration and the configuration management database!).

This project is intended to eventually be a replacement for tools such as Spacewalk and Cobbler and we hope that the REST API will enable integration with tools such as Puppet, Chef and Mcollective to be flexible and include other tools over time.

There is currently a *very* limited web interface (the only thing you can do is list items in the Configuration Management Database) however the bog-standard DJango admin interface does work (albeit long-winded!) for adding new items to the CMDB/CMS/Orchestra apps.

## So what's the current status? 

I can't stress this strongly enough:- **This project is not even in Alpha Testing yet!**

We currently have the models created for the following modules:

*   Configuration Management DataBase (CMDB)
*   Change Management System
*   Orchestra (Integration with tools such as Puppet etc)
*   Auditorium (An audit framework - yet to be properly worked on)

We also have a very basic API that allows you to query the system via FQDN and either return some information about the system (Rack, Datacentre, Configuration Item Owner etc) or return the classes and metadata used by Puppet.

A script is also available in the 'contrib' directory that can be placed in /var/lib/puppet/lib/facter to convert the above into Facts for use in both Puppet and Mcollective as well as a basic apache config file to enable service edison via wsgi.  The third script in that directory is copied (almost in its entirity!) from [The Cobbler Project][3] and allows you to use edison as an external lookup for puppet nodes so you can tie your CMDB and Configuration Management tools together.

## How do I get started?

There is a document named "HOWTO.md" in the docs directory of the source-code.

## Can I get involved? 

We're more than happy to take suggestions, however for the moment there is no intention to add extra people to the team as we're still not 100% sure where we're headed!

If there's something you'd like to see and it's not on the [Wishlist][1], create a ticket on the [issues page][2] and we'll get to it as soon as we can!

As soon as we feel that we've got a good idea on where we're headed, we'll get in contact with all those who want to help and give you write access to the source...

Also, don't forget that this is github, feel free to fork the code (paying attention to the license of course!) and send us a pull request if you make any major changes!

[1]: http://github.com/proffalken/edison/wiki/WishList
[2]: http://github.com/proffalken/edison/issues
[3]: https://fedorahosted.org/cobbler/
