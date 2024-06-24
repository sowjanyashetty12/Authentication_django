from django.shortcuts import render , HttpResponse , redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def homepage(request):
    return render(request,"index.html")
def register(request):
    
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
           
            messages.success(request,"registered")
            return redirect("login")
        else:
            messages.error(request,"invalid")
    else:
        form=UserCreationForm()
    context={
           'registerform':form
       }
    return render(request,"register.html",context)
def login_view(request):
    if request.method=="POST":
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
         login(request,form.get_user())
         return redirect("dashboard")
    else:
        form=AuthenticationForm()
    return render(request,"login.html",{"loginform":form})
@login_required(login_url="login")
def dashboard(request):
    if request.method=="POST":
        logout(request)
        return render(request,"index.html")
    else:
        return render(request,"dashboard.html")


