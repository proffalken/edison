# This file is part of the Edison Project.
# Please refer to the LICENSE document that was supplied with this software for information on how it can be used.
from django.test import TestCase
from django.test.client import Client

class LoginTest(TestCase):
    fixtures = ['../initial_data.json']

    def setUp(self):
        # Setup the client 
        client = Client()
 
    def test_response(self):
        # get the index page
        response = self.client.get('/accounts/login/',{'username':'admin','password':'password'})

	# Check we have recieved a '200' response
	self.failUnlessEqual(response.status_code,200)

class KickstartTest(TestCase):
    fixtures = ['../initial_data.json']
    def setUp(self):
        client = Client()

    def test_kickstart(self):
        response = self.client.get('/api/kickstart/', HTTP_X_RHN_PROVISIONING_MAC_0='eth0 aa:bb:cc:dd:ee:ff' )

	self.failUnlessEqual(response.content,'# NO KICKSTART REQUIRED #')
