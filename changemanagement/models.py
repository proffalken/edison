# This file is part of the Edison Project.
# Please refer to the LICENSE document that was supplied with this software for information on how it can be used.
import datetime
from django.db import models
from django.contrib.auth.models import User
from cmdb.models import ConfigurationItem

# Models for Change Management System
class ChangeStatus(models.Model):
	Description = models.CharField(max_length=128)
	ClosesChangeRequest = models.BooleanField()

	def __unicode__(self):
		return self.Description

	class Meta:
		verbose_name = 'Current Status'
		verbose_name_plural = 'Change Statuses'

class Scmtype(models.Model):
	Name = models.CharField(max_length=50)
	LibraryName = models.CharField(max_length=255)

	def __unicode__(self):
		return self.Name

	class Meta:
		verbose_name = 'Source Code Management Tool'
		ordering = ['Name']

class ScmRepo(models.Model):
	Scm = models.ForeignKey(Scmtype)
	Url = models.CharField(max_length=255)
	Name = models.CharField(max_length=255)
	Description = models.CharField(max_length=255)

	def __unicode__(self):
		return self.Name

	class Meta:
		verbose_name = 'Source Code Management Repository'
		verbose_name_plural = 'Source Code Management Repositories'
		ordering = ['Name']

class ChangeHeader(models.Model):
	Title = models.CharField(max_length=255)
	Requestor = models.ForeignKey(User)
	Summary = models.TextField()
	AffectedItems = models.ManyToManyField(ConfigurationItem)
	ScmRepo = models.ForeignKey(ScmRepo)
        Created = models.DateField()
    	Due = models.DateTimeField()	
	Status = models.ForeignKey(ChangeStatus)
	Completed = models.BooleanField(editable=False)
    
	def save(self):
		if not self.id:
	        	self.created = datetime.date.today()
	        super(ChangeHeader, self).save()

	def __unicode__(self):
		return self.Title

	class Meta:
		verbose_name = 'Change Request Header'
		verbose_name_plural = 'Change Request Headers'
		ordering = ['Title']

class Details(models.Model):
	Header = models.ForeignKey(ChangeHeader)
	Description = models.TextField()
	GitCommit = models.CharField(max_length=255)
	Created = models.DateTimeField()
	UpdatedBy = models.ForeignKey(User)
	
	def save(self):
		if not self.id:
	        	self.created = datetime.date.today()
	        super(Details, self).save()

	def __unicode__(self):
		return self.Description

	class Meta:
		verbose_name = 'Change Request Detail'
		verbose_name_plural = 'Change Request Details'
		ordering = ['Description']

