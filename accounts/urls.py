from django.urls import path

from . import views

app_name = 'accounts'
urlpatterns = [
    path('',views.index, name='doctor_list'),
    path('login/',views.login, name='login'),
    path('signup/',views.signup, name='signup'),    
    path('profile/<slug:slug>/',views.doctor_profile,name='doctor_profile'),
    path('myprofile/',views.my_profile,name='profile'),
]

