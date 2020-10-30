from django import forms
from django.contrib.auth.models import User
class RegisterForm(forms.Form):
    email = forms.EmailField(max_length=100)
    username = forms.CharField(max_length=100)
    password1= forms.CharField(widget=forms.PasswordInput())
    password2= forms.CharField(widget=forms.PasswordInput())

    def save(self):
        User.objects.create_user(username=self.cleaned_data['username'], email =self.cleaned_data['email'], password=self.cleaned_data['password1'])
