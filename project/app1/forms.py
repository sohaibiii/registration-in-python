from django import forms
from django.contrib.auth.models import User
from app1.models import userprofile

class userform(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput)
    class Meta():
        model = User
        fields = ('username','email','password')

class userprofileform(forms.ModelForm):
    class Meta():
        model =userprofile
        fields =('portfoliourl','portfoliopic')
