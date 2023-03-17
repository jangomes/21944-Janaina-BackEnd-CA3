21944 - Janaina Gomes

<h2> BSC30921 - Back-end Web Development - Continuous Assessment 3 </h2>

- <h4> ASSIGNMENT SOLUTION:</h4>

Basically, the testing methodology used is a combination of manual and automated testing. Manual testing is performed using the Django test client, which sends HTTP requests to the application and verifies the responses. In this case, the manual tests are verifying that the status code is 200 and that the correct template is being used for the enrollment page.
Automated testing is performed using the pytest-django library, which allows for more dynamic testing of Django applications. The tests are generating test data for the user form and using the RequestFactory to create test requests for the SignUpView. The tests are verifying that the status code and URL are correct for the success case and that the correct template is being used for the failure case.
The test coverage for this code is focused on the app's subscription functionality. He is testing that the sign-up page is accessible, the correct template is being used, and the sign-up form is working. It's also testing success and failure cases for the signup form, ensuring the application handles errors properly. 

To make the code more secure, I used cross-site scripting (xss) protection using Django's built-in security features. In my setting.py I added a line in the middleware adds the x-xss-protection header to HTTP responses, which instructs the browser to block any xss attacks. I used Django's  class to parse the request's query parameters, and validate them before passing them to the database query, I used Django's Q objects to construct the where clause of the SQL query in a way that prevents SQL injection attacks.



<h4> Bibliography: </h4>

Docs, R. t. (n.d.). Making queries. Retrieved from Django: https://docs.djangoproject.com/en/3.2/topics/db/queries/#complex-lookups-with-q-objects

Docs, R. t. (n.d.). Middleware. Retrieved from Django: https://docs.djangoproject.com/en/4.1/ref/middleware/

Docs, R. t. (n.d.). Testing in Django. Retrieved from Django: https://docs.djangoproject.com/en/3.2/topics/testing/

Santos, A. And Herman, M.  (n.d.). Testing in Django (Part 1) – Best Practices and Examples. Retrieved from Real Python: https://realpython.com/testing-in-django-part-1-best-practices-and-examples/

Docs, R. t. (n.d.). Writing your first Django app. Retrieved from Django: https://docs.djangoproject.com/en/4.1/intro/tutorial01/

Vincent, W. (2022, March 22). Django Login and Logout Tutorial. Retrieved from LearnDjango: https://learndjango.com/tutorials/django-login-and-logout-tutorial

Vincent, W. (2022, March 22). Django Password Reset Tutorial. Retrieved from LearnDjango: https://learndjango.com/tutorials/django-password-reset-tutorial

Vincent, W. (2022, March 11). Django Signup Tutorial. Retrieved from LearnDjango: https://learndjango.com/tutorials/django-signup-tutorial
