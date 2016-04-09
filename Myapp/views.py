from django.shortcuts import render
from django.views.generic.list import ListView
from django.http import HttpResponse, HttpResponseRedirect
import json
from .forms import CommentForm
from .models import Person, Location, Comment
from django.core import serializers

# Create your views here.

def home(request):
	if request.method == 'POST':
		form = CommentForm(request.POST)
		person = Person()
		if form.is_valid():
			# first_name = form.cleaned_data['first_name']
			# last_name = form.cleaned_data['last_name']
			# middle_name = form.cleaned_data['middle_name']
			# telephone = form.cleaned_data['telephone']
			# email = form.cleaned_data['email']
			# region = form.cleaned_data['region']
			# sity = form.cleaned_data['sity']
			# instance = form.save(commit=False)
			# first_name = person.first_name
			

			return HttpResponseRedirect("/admin")
	else:
		form = CommentForm()
	return render(request, "base.html", {'form':form})


def ajax(request):
    if request.method == 'POST':
        response_data = {}
        
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        middle_name = request.POST.get('middle_name')
        telephone = request.POST.get('telephone')
        email = request.POST.get('email')
        region = request.POST.get('region')
        sity = request.POST.get('sity')

        location = Location.objects.create(region=region,sity=sity)
        person = Person.objects.create(first_name=first_name, last_name=last_name, 
        	middle_name=middle_name,telephone = telephone, email=email)
      

        response_data['result'] = 'Create  POST successful!'
        response_data['first_name'] = first_name
        response_data['last_name'] = last_name
        response_data['region'] = region
        response_data['sity'] = sity
        response_data['email-text'] = email
       
        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )







