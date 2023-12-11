from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseBadRequest
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
# from .models import related models
# from .restapis import related methods
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from datetime import datetime
import logging
import json

from django.contrib.auth import login, login, authenticate
from django.views.decorators.http import require_POST

# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.


# Create an `about` view to render a static about page
def about(request):
    return render(request, "about.html")


# Create a `contact` view to return a static contact page
def contact(request):
    return render(request, "contact.html")

# Create a `login_request` view to handle sign in request
def login_request(request):
    user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('djangoapp:index'))
    return redirect('djangoapp:index')

# Create a `logout_request` view to handle sign out request
@require_POST
def logout_request(request):
    logout(request)
    return redirect('djangoapp:index')

# Create a `registration_request` view to handle sign up request
def registration_request(request):
    if request.method == 'GET':
        return render(request, "djangoapp/registration.html")
    elif request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        password = request.POST['password']

        try:
            User.objects.get(username=username)
            
            return render(request, "djangoapp/registration.html")
        except User.DoesNotExist:
            user = User.objects.create_user(username=username, 
                first_name=firstname, 
                last_name=lastname, 
                password=password
            )
            return redirect('djangoapp:index')

# Update the `get_dealerships` view to render the index page with a list of dealerships
def get_dealerships(request):
    context = {}
    if request.method == "GET":
        return render(request, 'djangoapp/index.html', context)


# Create a `get_dealer_details` view to render the reviews of a dealer
# def get_dealer_details(request, dealer_id):
# ...

# Create a `add_review` view to submit a review
# def add_review(request, dealer_id):
# ...

