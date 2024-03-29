from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,get_object_or_404
from .forms import RegistrationForm

from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.models import Group
from django.contrib import messages

def register_user(request):
    if request.method=="POST":
        form=RegistrationForm(request.POST or None)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            firstname = form.cleaned_data.get('first_name')
            lastname = form.cleaned_data.get('last_name')
            user=authenticate(username=username,password=password)
            user.first_name = firstname
            user.last_name = lastname
            user.save()
            login(request,user)
            messages.success(request,"Welcome {}".format(username))
            return HttpResponseRedirect(reverse('core:home'))
        else:
            messages.error(request,form.errors)
            return render(request,"account/signup.html",{'form':form})
    else:
        form=RegistrationForm()
        return render(request,"account/signup.html",{'form':form})