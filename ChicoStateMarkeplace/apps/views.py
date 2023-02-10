# pylint: disable=superfluous-parens
from unicodedata import category
from django.shortcuts import render, redirect
from django.http import HttpResponse
import apps
from django.urls import reverse

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.

def join(request):
    if (request.method == "POST"):
        join_form = JoinForm(request.POST)
        if (join_form.is_valid()):
            # Save form data to DB
            user = join_form.save()
            # Encrypt the password
            user.set_password(user.password)
            # Save encrypted password to DB
            user.save()
            # Success! Redirect to home page.
            return redirect("/")
        else:
            # Form invalid, print errors to console
            page_data = {"join_form": join_form}
            return render(request, 'app1/join.html', page_data)
    else:
        join_form = JoinForm()
        page_data = {"join_form": join_form}
        return render(request, 'app1/join.html', page_data)

def home(request):
    return render(request, 'home/home.html')

def about(request):
    return render(request, 'about/about.html')

def messaging(request):
    return render(request, 'messaging/messaging.html')

def savedpost(request):
    return render(request, 'savedPost/saved.html' )

