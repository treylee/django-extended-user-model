from django.test import TestCase
from user.models import Customer
from django.contrib.auth.models import User
class AnimalTestCase(TestCase):
    def setUp(self):
        u = User.objects.create(username="trey",password="checking")
        c = Customer.objects.create(user=u,department="treysdep", age=31)
        c.save()

    def test__adding_fields__to_usermodel(self):
        """Animals that can speak are correctly identified"""
        u = User.objects.get(username="trey",password="checking")
        
        self.assertEqual(u.customer.age, 31)
        self.assertEqual(u.customer.department, "treysdep")

