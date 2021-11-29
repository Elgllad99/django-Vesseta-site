from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db.models import fields




class UserCreationForm(UserCreationForm):
    username =  forms.CharField(label='الاسم')
    first_name = forms.CharField(label='الاسم الاول')
    last_name = forms.CharField(label='الاسم الاخير')
    email = forms.EmailField(label='البريد الالكتروني')
    password=forms.CharField(label='كلمة السر',widget=forms.PasswordInput(),min_length=8)
    password2=forms.CharField(label='تأكيد كلمه السر',widget=forms.PasswordInput(),min_length=8)
    
    class Meta:
        model = User
        fields=('username','first_name','last_name','email','password','password2')
    
    
class Login_Form(forms.ModelForm):
    username = forms.CharField(label='الاسم')
    password = forms.CharField(label="كلمه السر",widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ('username','password')