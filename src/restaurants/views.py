from django.http import HttpResponse
from django.shortcuts import render
import random

# Create your views here.
# function based request 
def home(request):
#	return HttpResponse("hello")
	num = random.randint(0, 10000)
	some_text = "see this"
	context = {
		"bool_item": True,
		"numcheck": num,
		"some_text": some_text
	}
	return render(request, "home.html", context) 

def about(request):
#	return HttpResponse("hello")
	num = random.randint(0, 10000)
	some_text = "see this"
	context = {
		"bool_item": True,
		"numcheck": num,
		"some_text": some_text
	}
	return render(request, "about.html", context) 

def contact(request):
#	return HttpResponse("hello")
	num = random.randint(0, 10000)
	some_text = "see this"
	context = {
		"bool_item": True,
		"numcheck": num,
		"some_text": some_text
	}
	return render(request, "contact.html", context) 