# This file is part of the Edison Project.
# Please refer to the LICENSE document that was supplied with this software for information on how it can be used.
from django.db import models
from cmdb.models import ConfigurationItem
# Create your models here.

# log the packages that are updated every time the package manager runs
#
# Need to write a yum/apt-plugin to post to the API for this...
class Package(models.Model):
	Name = models.CharField(max_length=255)
	Version = models.CharField(max_length=255)
	Repository = models.CharField(max_length=255)
	AffectedItem = models.ForeignKey(ConfigurationItem)
	DateApplied = models.DateTimeField()

	def __unicode__(self):
		return u'%s - %s' % (self.Name,self.Version)

	class Meta:
		verbose_name = 'Software Package'
		verbose_name_plural = 'Software Packages'
		ordering = ['Name','Version']


