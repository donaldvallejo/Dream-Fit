# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from accounts.models import Testuser

class userTests(TestCase):
    def test_True(self):
        # Create two objects of type List.
        Testuser.objects.create(name="bryan", email="dude69@pornhub.com", password="69p0rn3ub")
        Testuser.objects.create(name="donny", email="girl96@pornhub.com", password="pron69696")
        
        # Get created objects of type list from db 
        bryan = Testuser.objects.get(name="bryan")
        donny = Testuser.objects.get(name="donny")

        # Call test assertions
        self.assertEqual(bryan.__str__(), "bryan | dude69@pornhub.com | 69p0rn3ub")
        self.assertEqual(donny.__str__(), "donny | girl96@pornhub.com | pron69696")

    def test_False(self):
        # Create two objects of type List.
        Testuser.objects.create(name="guy", email="dudeee465@pornhub.com", password="smfnsd35nf")
        Testuser.objects.create(name="girl", email="giirlr435@pornhub.com", password="whadupypo45")
        
        # Get created objects of type list from db 
        guy = Testuser.objects.get(name="guy")
        girl = Testuser.objects.get(name="girl")

        # Call test assertions
        self.assertNotEqual(guy.__str__(), "guy | dsfgsdf57789@pornhub.com | 69sdgg3ub")
        self.assertNotEqual(girl.__str__(), "girl | gifgdsf567@pornhub.com | pron457454")

