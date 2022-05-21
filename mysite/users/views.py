from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method=="POST":
        form= UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get("username")
            messages.success(request,f"Your account {user} has been registered. You can now log in ")
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request,"users/register.html",{'form':form})
    return HttpResponse("Welcome to register page")

@login_required
def profile(request):
    return render(request,"users/profile.html")