from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView

""" First part: this point the root URLconf at the polls.urls  """
urlpatterns = [

    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path("accounts/", include("accounts.urls")),
    # included in the first part of the tutorial
    path("accounts/", include("django.contrib.auth.urls")),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
]
