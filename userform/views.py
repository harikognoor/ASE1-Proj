from django.shortcuts import render
from userform.forms import userform
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.http import HttpResponse
# Create your views here.
def register(request):
    registered=False
    if request.method =="POST":
        user_form=userform(data=request.POST)

        if user_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()
            registered=True
        else:
            print(userform.errors)
    else:
        user_form =userform()
    return render(request,'userform/registration.html',{'user_form':user_form,'registered':registered})

@login_required
def log_out(request):
    return render(request,'userform/registration.html')
@login_required
def special(request):
    return HttpResponse(loggedin)




def user_login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponse("<h1>account logged in</h1>")
            else:
                 return HttpResponse("account not active")
        else:
            print("username:{} and password{}".format(username,password))
            return HttpResponse("<h1>invalid details</h1>")
    else:
        return render(request,'userform/login.html',{})
