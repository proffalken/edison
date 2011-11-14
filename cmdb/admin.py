# This file is part of the Edison Project.
# Please refer to the LICENSE document that was supplied with this software for information on how it can be used.
# ensure that we include all the models required to administer this app
from cmdb.models import *
from django.contrib import admin

admin.site.register(Country)
admin.site.register(County)
admin.site.register(Address)
admin.site.register(Company)
admin.site.register(Contact)
admin.site.register(DataCentre)
admin.site.register(DataCentreRoom)
admin.site.register(DataCentreSuite)
admin.site.register(DataCentreRack)
admin.site.register(Repo)
admin.site.register(ConfigurationItemClass)
admin.site.register(NetworkInterface)
admin.site.register(PackageProvider)
admin.site.register(PackageFormat)
admin.site.register(OperatingSystemBreed)
admin.site.register(OperatingSystemName)
admin.site.register(OperatingSystemVersion)
admin.site.register(VirtualisationType)
admin.site.register(VirtualServerDefinition)
admin.site.register(ConfigurationItemProfile)
admin.site.register(ConfigurationItem)
