from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
import random
from .models import RestaurantLocation

# Create your views here.
# function based request 
class HomeView(TemplateView):
	template_name = 'home.html'	
	'''def get_context_data(self, *args, **kwargs): 
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
		return context '''

#this is a list view that uses one template to show filters and all the data
class RestaurantListView(ListView):
	def get_queryset(self):
		print (self.kwargs)
		slug = self.kwargs.get("slug")
		if slug:
			queryset = RestaurantLocation.objects.filter(
				Q(category__iexact=slug) |
				Q(category__icontains=slug)
			)
		else:
			queryset = RestaurantLocation.objects.all()
			print
		return queryset
# this is for the detail view of the product 
class RestaurantDetailView(DetailView):
	queryset = RestaurantLocation.objects.all()

	 #this is to check what is the coming in get url and wht is it fetching
	'''def get_context_data(self, *args, **kwargs):
		print(self.kwargs)
		context = super(RestaurantDetailView, self).get_context_data(*args, **kwargs)
		print(context)
		return context'''

	def get_object(self, *args, **kwargs):
		rest_id = self.kwargs.get("rest_id")
		obj = get_object_or_404(RestaurantLocation, id = rest_id) #pk = rest_id (it makes the rest id equal to default django get url keywords)
		return obj








