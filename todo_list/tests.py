from django.contrib.auth.models import User
from django.test import TestCase
from todo_list.models import List

class ListTests(TestCase):
    def test_True(self):
        # Create two objects of type List.
        List.objects.create(item="bryans_stuff", price=10.00, quantity=2, completed=False)
        List.objects.create(item="donnys_stuff", price=100.00, quantity=3, completed=False)
        
        # Get created objects of type list from db 
        bryans_stuff = List.objects.get(item="bryans_stuff")
        donnys_stuff = List.objects.get(item="donnys_stuff")

        # Call test assertions
        self.assertEqual(bryans_stuff.__str__(), "bryans_stuff | 10.00 | 2 | False")
        self.assertEqual(donnys_stuff.__str__(), "donnys_stuff | 100.00 | 3 | False")

    def test_False(self):
        # Create two objects of type List.
        List.objects.create(item="bryan", price=1.00, quantity=1, completed=True)
        List.objects.create(item="donny", price=1.00, quantity=1, completed=True)
        
        # Get created objects of type list from db 
        bryan = List.objects.get(item="bryan")
        donny = List.objects.get(item="donny")

        # Call test assertions
        self.assertNotEqual(bryan.__str__(), "bryan | 1.00 | 2 | True")
        self.assertNotEqual(donny.__str__(), "donny | 1.00 | 2 | True")
