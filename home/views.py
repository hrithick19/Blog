from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from .forms import Contact_form

def index(request):
    template="home/home.html"
    nav=["active","","",""]   
    context={'nav':nav}
    return render(request,template,context)

def about(request):
    template="home/about.html"
    nav=["","active","",""]
    context={'nav':nav}
    return render(request,template,context)

def contact(request):
    nav=["","","","active"]
    form=Contact_form(request.POST or None)
    if form.is_valid():
        form.save()
        form=Contact_form()
    template="home/contact.html"
    context={
        'form':form,
        'nav':nav
    }
    return render(request,template,context)

