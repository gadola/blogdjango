from django import forms
import re
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth.models import User




class RegisterForm(forms.Form):
    email = forms.EmailField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control margin-bottom-20","required":""}))
    username = forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control margin-bottom-20","required":""}))
    password1= forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control margin-bottom-20","required":""}))
    password2= forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control margin-bottom-20","required":""}))

    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2 and password1:
                return password2
        raise forms.ValidationError("Mật khẩu không hợp lệ")
    
    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError("Tên tài khoản có kí tự đặc biệt")
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError("Tài khoản đã tồn tại")

    def save(self):
        User.objects.create_user(username=self.cleaned_data['username'], email =self.cleaned_data['email'], password=self.cleaned_data['password1'])

            
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus': True,"class":"form-control"}))
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={"class":"form-control"}),
    )