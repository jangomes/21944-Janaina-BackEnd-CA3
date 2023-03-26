from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
import unittest

# CA3 Add testing using one of the unit test libraries and one or more module/function.
#File for development

# python manage.py test accounts.tests
# I used pip install pytest to install the pytest library


# run the test with this code: python manage.py test accounts.tests
class TestSignUpView(TestCase):

    # This is a Django built in test client to test the sign up page
    def test_signup_page_status_code(self):
        response = self.client.get('/signup/')
        self.assertEqual(response.status_code, 200)
    #I am checking whether the status code is 200 and whether the correct template is being used
    def test_signup_page_template(self):
        response = self.client.get('/signup/')
        self.assertTemplateUsed(response, 'registration/signup.html')

if __name__ == '__main__':
    unittest.main()
