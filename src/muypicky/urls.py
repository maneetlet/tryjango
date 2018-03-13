"""muypicky URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView

from restaurants.views import (HomeView, RestaurantListView, RestaurantDetailView, )

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view()),
    #this is done for static templates that do not have anything in views to be dynamicly fetched 
    url(r'^about/$', TemplateView.as_view(template_name= 'about.html')),
    url(r'^contact/$', TemplateView.as_view(template_name= 'contact.html')),
    #till here
    #We need to write both the url without parameter and url with parameters passed in 
    url(r'^restaurants/$', RestaurantListView.as_view()),
    #url(r'^restaurants/(?P<slug>\w+)/$', RestaurantListView.as_view()),
    #slug is mentioned just to tell the parameter after the url is the slug 
    #the details veiw in restaurant passs the id or pk primary key 
    #url(r'^restaurants/(?P<pk>\w+)/$', RestaurantDetailView.as_view()),
    #this is not the default (slug pk or id) this is my own stated get key word argument rest_id it could be anything 
    url(r'^restaurants/(?P<rest_id>\w+)/$', RestaurantDetailView.as_view()),
]
