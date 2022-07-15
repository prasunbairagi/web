from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login
# Create your views here.
def  Signup(request):
    signupform=UserCreationForm(request.POST or None)
    if signupform.is_valid():
        signupform.save()
        email=signupform.cleaned_data.get('email')
        username=signupform.cleaned_data.get('username')#getting the vlaue from user for username
        raw_password=signupform.cleaned_data.get('password1')#getting the value from user for password
        user=authenticate(email=email,username=username,password=raw_password)#checking wethaer password or username is equal or not acc to database
        login(request,user)#if username and password are equal then it will login
        return redirect('todolist')# and redirect to feedback page
    return render(request,'signup.html',{'form':signupform})#otherwise it will be at the same page of signup
