from django import forms
from django.contrib.auth import  get_user_model
from userform.models import userprofile
User = get_user_model()

class userform(forms.ModelForm):
    password= forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model=User
        fields=('username','email','password')
