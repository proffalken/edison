# This file is part of the Edison Project.
# Please refer to the LICENSE document that was supplied with this software for information on how it can be used.
from django.db import models
from django.contrib.auth.models import User

# These are the models required for the basic CMDB

# First, Define our list of countries
class Country(models.Model):
    Name = models.CharField(max_length=255)
    Code = models.CharField(max_length=3)

    def __unicode__(self):
        return self.Code
    
    class Meta:
        #permissions = ()
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'
        ordering = ['Name']
    
    
# Now define the counties/States that we can use
class County(models.Model):
    Name = models.CharField(max_length=128)
    Country = models.ForeignKey('Country')
    
    def __unicode__(self):
        return self.Name
    
    class Meta:
        #permissions = ()
        verbose_name = 'County'
        verbose_name_plural = 'Counties'
        ordering = ['Name']

# Where do people/things live?
class Address(models.Model):
    LineOne = models.CharField(max_length=128)
    LineTwo = models.CharField(max_length=128,blank=True)
    LineThree = models.CharField(max_length=128,blank=True)
    Postcode = models.CharField(max_length=15)
    County = models.ForeignKey('County')
    Country = models.ForeignKey('Country') 

    def __unicode__(self):
        return u'%s, %s, %s' % (self.LineOne, self.County, self.Postcode)
    
    class Meta:
        #permissions = ()
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'
        ordering = ['LineOne']

# What companies are there that we might want to talk to?
class Company(models.Model):
    Name = models.CharField(max_length=255)
    HeadOffice = models.ForeignKey('Address')
    SupportNumber = models.CharField(max_length=50)
    SupportEmail = models.EmailField()
        
    def __unicode__(self):
        return self.Name
    
    class Meta:
        #permissions = ()
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'
        ordering = ['Name']
    
# A list of all our contacts both within and external to the company we work for
class Contact(models.Model):
    TITLE_CHOICES = (
                     ('Mr','Mr'),
                     ('Mrs','Mrs'),
                     ('Miss','Miss'),
                     ('Ms','Ms')
                     )
    Title = models.CharField(max_length=6,choices=TITLE_CHOICES)
    FirstName = models.CharField(max_length=128)
    LastName = models.CharField(max_length=128)
    PrimaryPhone = models.CharField(max_length=50)
    EmailAddress = models.EmailField()
    Company = models.ForeignKey('Company')
    
    def __unicode__(self):
        return u'%s %s %s' % (self.Title, self.FirstName, self.LastName)
    
    class Meta:
        #permissions = ()
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
        ordering = ['FirstName']

    
# Our Datacentres
class DataCentre(models.Model):
    Name = models.CharField(max_length=255)
    ShortCode = models.CharField(max_length=10)
    Address = models.ForeignKey('Address')
    PrincipleContact = models.ForeignKey('Contact')

    def __unicode__(self):
        return self.ShortCode
    
    class Meta:
        #permissions = ()
        verbose_name = 'Data Centre'
        verbose_name_plural = 'Data Centres'
        ordering = ['Name']

# The rooms in the datacentres
class DataCentreRoom(models.Model):
    RoomName = models.CharField(max_length=25)
    DataCentre = models.ForeignKey('DataCentre')
    
    def __unicode__(self):
        return u'%s in %s' % (self.RoomName, self.DataCentre)
    
    class Meta:
        #permissions = ()
        verbose_name = 'Data Centre Room'
        verbose_name_plural = 'Data Centre Rooms'
        ordering = ['RoomName']
    
# The suites in the datacentres
class DataCentreSuite(models.Model):
    SuiteName = models.CharField(max_length=128)
    Room = models.ForeignKey('DataCentreRoom')
    
    def __unicode__(self):
        return u'%s -> %s' % (self.SuiteName, self.Room)
    
    class Meta:
        #permissions = ()
        verbose_name = 'Data Centre Suite'
        verbose_name_plural = 'Data Centre Suites'
        ordering = ['SuiteName']

# The racks in the suites in the rooms in the datacentres....
class DataCentreRack(models.Model):
    RackName = models.CharField(max_length=25)
    Room = models.ForeignKey('DataCentreRoom',blank=True)
    Suite= models.ForeignKey('DataCentreSuite',blank=True)
    
    def __unicode__(self):
        return u'%s -> %s (%s)' % (self.RackName, self.Suite, self.Room)
    
    class Meta:
        #permissions = ()
        verbose_name = 'Data Centre Rack'
        verbose_name_plural = 'Data Centre Racks'
        ordering = ['RackName']

# The different classes of configuration items
class ConfigurationItemClass(models.Model):
    Name = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.Name
    
    class Meta:
        #permissions = ()
        verbose_name = 'Configuration Item Class'
        verbose_name_plural = 'Configuration Item Classes'
        ordering = ['Name']

# The network interfaces that are assigned to configuration items
class NetworkInterface(models.Model):
    Name = models.CharField(max_length=5)
    MacAddress = models.CharField(max_length=30)
    Gateway = models.IPAddressField(blank=True, null=True)
    SubnetMask = models.IPAddressField(blank=True, null=True)
    IPAddress = models.IPAddressField(blank=True, null=True)
    UseDHCP = models.BooleanField()

    def __unicode__(self):
        return u'%s (%s -> %s)' % (self.Name, self.IPAddress, self.MacAddress)    
    
    class Meta:
        #permissions = ()
        verbose_name = 'Network Interface'
        verbose_name_plural = 'Network Interfaces'
        ordering = ['Name']

class PackageProvider(models.Model):
    Name = models.CharField(max_length=255)
    ExecutableName = models.CharField(max_length=255)

    def __unicode__(self):
        return self.Name

class PackageFormat(models.Model):
    Name = models.CharField(max_length=255)
    Provider = models.ForeignKey(PackageProvider)

    def __unicode__(self):
        return self.Name

class Repo(models.Model):
    Name = models.CharField(max_length=255)
    PackageProvider = models.ForeignKey(PackageProvider)
    url = models.CharField(max_length=255)

    def __unicode__(self):
        return self.Name


class OperatingSystemBreed(models.Model):
    Name = models.CharField(max_length=255)
    PackageFormat = models.ForeignKey(PackageFormat)

    def __unicode__(self):
        return self.Name

class OperatingSystemName(models.Model):
    Name = models.CharField(max_length=200)
    SupportCompany = models.ForeignKey(Company)
    Breed = models.ForeignKey(OperatingSystemBreed)

    def __unicode__(self):
        return u'%s supported by %s' % (self.Name, self.SupportCompany)

class OperatingSystemVersion(models.Model):
    Name = models.ForeignKey(OperatingSystemName)
    Version = models.CharField(max_length=128)
    EOLDate = models.DateField(blank=True, null=True, verbose_name='End of Life Date')
    EOSDate = models.DateField(blank=True, null=True, verbose_name='End of Support Date')
    
    def __unicode__(self):
        return u'%s %s' % (self.Name,self.Version)

# the following classes are based on the libvirt xml standard, although they do not contain all the possible options
class VirtualisationType(models.Model):
    Name = models.CharField(max_length=128)
    Description = models.CharField(max_length=255)

    def __unicode__(self):
        return self.Name

    class Meta:
        verbose_name = 'Virtualisation Type'
	verbose_name_plural = 'Virtualisation Types'
	ordering = ['Name']

class VirtualServerDefinition(models.Model):
    Name = models.CharField(max_length=255)
    NumCPU = models.IntegerField(max_length=4)
    RamMB = models.IntegerField(max_length=7)
    DeployTo = models.ForeignKey('ConfigurationItem',null=True,blank=True)
    DiskSizeGB = models.IntegerField(default=8,max_length=7)
    POWER_CHOICES = (
    	('reboot','Reboot'),
	('destroy','Destroy'),
	('preserve','Preserve'),
	('coredump-destroy','Core Dump & Destroy'),
	('coredump-restart','Core Dump & Restart'),
    )
    OnReboot = models.CharField(max_length=25,choices=POWER_CHOICES)
    OnCrash = models.CharField(max_length=25,choices=POWER_CHOICES)
    OnPowerOff = models.CharField(max_length=25,choices=POWER_CHOICES)
    Acpi = models.BooleanField()
    Pae = models.BooleanField()
    NETWORK_CHOICES = (
        ('network','Virtual Network'),
	('bridge','LAN Bridge'),
	('user','Userspace SLIRP Stack'),
    )
    NetworkType = models.CharField(max_length=10,choices=NETWORK_CHOICES)
    BridgeNetworkInterface = models.CharField(max_length=10)
    VMType = models.ForeignKey(VirtualisationType)

    def __unicode__(self):
        return u'%s (%s cpus, %s MB RAM, %s GB Storage, %s Network using %s and powered by %s)' % (self.Name,self.NumCPU,self.RamMB,self.DiskSizeGB,self.NetworkType,self.BridgeNetworkInterface,self.VMType)

# Configuration Item Profiles
class ConfigurationItemProfile(models.Model):
    Name = models.CharField(max_length=255)
    VirtualServerDefinition = models.ForeignKey(VirtualServerDefinition,blank=True,null=True)
    OperatingSystem = models.ForeignKey(OperatingSystemVersion)
    AutoInstallFile = models.TextField(help_text="Paste your Kickstart/Debian a-i/Windows unattend.txt in here")
    repos = models.ManyToManyField(Repo,blank=True,null=True)

	
    def __unicode__(self):
        return self.Name


# The configuration items (servers/switches etc)
class ConfigurationItem(models.Model):
    Hostname = models.CharField(max_length=255)
    Rack = models.ForeignKey('DataCentreRack')
    Asset = models.CharField(max_length=128)
    SupportTag = models.CharField(max_length=128)
    Class = models.ForeignKey(ConfigurationItemClass)
    Owner = models.ForeignKey(User)
    NetworkInterface = models.ManyToManyField(NetworkInterface)
    Profile = models.ForeignKey(ConfigurationItemProfile)
    VMImagePath = models.CharField(max_length=255,blank=True,null=True,verbose_name='Path for Virtual Images')
    IsVirtual = models.BooleanField()
    BuildOnNextBoot = models.BooleanField(verbose_name="PXE Build",help_text="Should this box be rebuilt the next time it is booted?")
    IsVMHost = models.BooleanField()
    rootpwhash = models.CharField(max_length=255)

    def __unicode__(self):
        return self.Hostname
    
    class Meta:
        #permissions = ()
        verbose_name = 'Configuration Item'
        verbose_name_plural = 'Configuration Items'
        ordering = ['Hostname']
        

