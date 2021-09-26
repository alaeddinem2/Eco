from django.contrib import messages
from django.contrib.auth import login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from student_mnagament_app.EmailBackEnd import EmailBackEnd


def showDempPage(request):
    return render(request,"demo.html")


def showLoginPage(request):
    return render(request,"login.html")

def doLogin(request):
    if request.method!="POST":
        return HttpResponse("<H2> Method Not Allowed")
    else:
        user=EmailBackEnd.authenticate(request,username=request.POST.get("email"),password=request.POST.get("password"))
        if user!=None:
            login(request,user)
            if user.user_type=="1":
                return HttpResponseRedirect("/admin_home")
            elif user.user_type=="2":
                return HttpResponse("staff Login")
            else :
                return HttpResponse("student login")


            return HttpResponseRedirect( "/admin_home")
        else:
            messages.error(request,"Invalid Login Details !")
            return HttpResponseRedirect("/")


def getUserDetails(request):
    if request.user!=None:
        return HttpResponse("user: "+ request.user.email + "  usertype :  "+ str(request.user.user_type))
    else:
        return HttpResponse("please Login first")





def logoutUser(request):
    logout(request)
    return HttpResponseRedirect("/")
