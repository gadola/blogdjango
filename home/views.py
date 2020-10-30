from django.shortcuts import render
from .forms import RegisterForm
from django.shortcuts import redirect
from django.views import View
from django.contrib.auth import login,authenticate
# Create your views here.


class Register(View):

    def get(self,request):
        form = RegisterForm()
        return render(request,'home/register.html',{"form":form})

    def post(self,request):
        form = RegisterForm()
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
        return render(request,'home/register.html',{"form":form})
            
# class Login(View):
#     def get(self,request):
#         return render(request,'home/login.html')

#     def post(self,request):
#         if request.method == 'POST':
#             data = request.POST
#             username = data.get('username')
#             password = data.get('password')
#             myuser = authenticate(username=username,password = password)
#             if myuser is None:
#                 return 
#             return redirect('home')
#         return render(request,'home/login.html')