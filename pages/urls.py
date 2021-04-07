# pages urls.py
from django.urls import path
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name = 'home.html'), name='home'),
    
    # we can also use the templateview directly here in the urls
    # not reccomended but possible """
]
