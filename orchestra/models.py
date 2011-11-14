# This file is part of the Edison Project.
# Please refer to the LICENSE document that was supplied with this software for information on how it can be used.
from django.db import models
from django.contrib.auth.models import User
from cmdb.models import ConfigurationItem

# Models for Orchestration App

# The model for orchestration classes (puppet/Chef etc)
class OrchestraClass(models.Model):
	Name = models.CharField(max_length=255)
	Creator = models.ForeignKey(User)
	Notes = models.TextField()
	AffectedItems = models.ManyToManyField(ConfigurationItem)

	def __unicode__(self):
		return self.Name

	class Meta:
		verbose_name = 'Orchestration Class'
		verbose_name_plural = 'Orchestration Classes'
		ordering = ['Name']

# Metadata to be provided for each cfgitem (Datacentre etc)
class OrchestraMetaDataName(models.Model):
	Name = models.CharField(max_length=255)
	
	def __unicode__(self):
		return self.Name

	class Meta:
		verbose_name = 'Orchestration Metadata'
		ordering = ['Name']

class OrchestraMetaDataValue(models.Model):
	Name = models.ForeignKey(OrchestraMetaDataName)
	Value = models.CharField(max_length=255)
	AffectedItems = models.ManyToManyField(ConfigurationItem)
 	
	def __unicode__(self):
		return u'%s = %s' % (self.Name,self.Value)
	
