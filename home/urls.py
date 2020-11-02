from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'home'

urlpatterns = [
    path('register/',views.Register.as_view(), name='register'),
    path('login/',views.Login.as_view(),name = 'login' ),
    path('logout/',auth_views.LogoutView.as_view(next_page="home:login"),name = 'logout' ),
]


