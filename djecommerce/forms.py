
from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


from django.contrib.auth.models import Group


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    # email = forms.EmailField(required=False)
    pass
    # first
    # class Meta:
    #     model = User
    #     fields= ['username','first_name','last_name','email','password1','password2']