from django.contrib.auth.models import User
from django.test import RequestFactory
from mixer.backend.django import mixer
from pytest_django.asserts import assertTemplateUsed
from accounts.views import SignUpView

import pytest

#CA3 Add automatic (dynamic) testing using one of the unit test libraries and one or more module/functions.
# File for testing

#Here I am using the pytest-django library to test the "signup" page and its generating test data for the user form

#this one for the test data
@pytest.fixture
def user_data():
    data = {
        'username': 'testuser',
        'password1': 'testpassword123',
        'password2': 'testpassword123',
    }
    return data

#this one for the test request factory
@pytest.fixture
def request_factory():
    return RequestFactory()


@pytest.fixture
def signup_view(request_factory):
    view = SignUpView.as_view()
    request = request_factory.get('/signup/')
    return view(request=request)

#this one for the test SignUpView for success and failure cases
#I am checking whether the status code and URL are correct for the success case and whether the correct template is being used for the failure case
@pytest.mark.django_db
class TestSignUpView:

    def test_view_signup_success(self, signup_view, user_data):
        request = signup_view.request
        request.method = 'POST'
        request.POST = user_data

        response = signup_view(request)

        assert response.status_code == 302
        assert response.url == '/login/'

    def test_view_signup_fail(self, signup_view):
        request = signup_view.request
        request.method = 'POST'
        request.POST = {}

        response = signup_view(request)

        assert response.status_code == 200
        assertTemplateUsed(response, 'registration/signup.html')
