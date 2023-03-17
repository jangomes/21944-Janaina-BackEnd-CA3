21944 - Janaina Gomes

BSC30921 - Back-end Web Development - Continuous Assessment 3

ASSIGNMENT SOLUTION:

Basically, the testing methodology used is a combination of manual and automated testing. Manual testing is performed using the Django test client, which sends HTTP requests to the application and verifies the responses. In this case, the manual tests are verifying that the status code is 200 and that the correct template is being used for the enrollment page.
Automated testing is performed using the pytest-django library, which allows for more dynamic testing of Django applications. The tests are generating test data for the user form and using the RequestFactory to create test requests for the SignUpView. The tests are verifying that the status code and URL are correct for the success case and that the correct template is being used for the failure case.
The test coverage for this code is focused on the app's subscription functionality. He is testing that the sign-up page is accessible, the correct template is being used, and the sign-up form is working. It's also testing success and failure cases for the signup form, ensuring the application handles errors properly.



Bibliography:

Docs, R. t. (n.d.). Testing in Django. Retrieved from Django: https://docs.djangoproject.com/en/3.2/topics/testing/

Santos, A. And Herman, M.  (n.d.). Testing in Django (Part 1) – Best Practices and Examples. Retrieved from Real Python: https://realpython.com/testing-in-django-part-1-best-practices-and-examples/

Docs, R. t. (n.d.). Writing your first Django app. Retrieved from Django: https://docs.djangoproject.com/en/4.1/intro/tutorial01/

Vincent, W. (2022, March 22). Django Login and Logout Tutorial. Retrieved from LearnDjango: https://learndjango.com/tutorials/django-login-and-logout-tutorial

Vincent, W. (2022, March 22). Django Password Reset Tutorial. Retrieved from LearnDjango: https://learndjango.com/tutorials/django-password-reset-tutorial

Vincent, W. (2022, March 11). Django Signup Tutorial. Retrieved from LearnDjango: https://learndjango.com/tutorials/django-signup-tutorial
