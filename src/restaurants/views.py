from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
import random
from .models import RestaurantLocation

# Create your views here.
# function based request 
class HomeView(TemplateView):
	template_name = 'home.html'	
	def get_context_data(self, *args, **kwargs): 
		context = super(HomeView, self).get_context_data(*args, **kwargs)
		template_name = 'home.html'
	#	return HttpResponse("hello")
		num = random.randint(0, 10000)
		some_text = "see this"
		context = {
			"bool_item": True,
			"numcheck": num,
			"some_text": some_text
		}
		return context 

class AboutView(TemplateView):
	template_name = 'about.html'
	

class ContactView(TemplateView):
	template_name = 'contact.html'

class RestaurantListView(TemplateView):
	template_name = 'restaurants/restaurants_list.html'
	def get_context_data(self, *args, **kwargs):
		context = super(RestaurantListView, self).get_context_data(*args, **kwargs)
		queryset = RestaurantLocation.objects.all()
		
		context = { 
					 "object_list" : queryset
			 		}
		return context


	"""def post (self, request, *args, **kwargs)
		context = {

		}
		return render(request, "contact.html", context)"""
	'''def put (self, request, *args, **kwargs):
		context = {

		}	
		return render(request, "contact.html", context)'''



