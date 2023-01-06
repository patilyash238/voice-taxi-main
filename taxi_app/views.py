from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages as msg
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import *
from . import forms
from . import models
import random
# Create your views here.
def home(request):
    context = {

    }
    return render(request, 'home.html', context)

def noti(request):
    context = {

    }
    msg.info(request, "This is a notification")
    return redirect('home')
    # return render(request, 'home.html', context)



def signinform(request):
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['UserName']
            password = request.POST['Password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                msg.info(request, "Welcome " + str(user.first_name))
                return redirect('home')
            else:
                msg.info(request, "ohh hell naw... Please check your creds...")
            return redirect('signinform')
    else:
        form = forms.LoginForm()

    context = {
        "form" : form
    }

    return render(request, 'login.html', context)

def signupform(request):

    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            try:
                user = User.objects.create_user(username = request.POST["UserName"], email = request.POST["Email"], first_name = request.POST["FirstName"], last_name = request.POST["LastName"], password = request.POST["Password"])
                msg.info(request, "Sign Up successful.")
            except NameError:
                msg.info(request, "SignUp failed please make your user unique and try again.")
                return redirect('signupform')
            except:
                msg.info(request, "<b style='color:red;'>Unknown Error...</b>")
                return redirect('signupform')
            return redirect('home')
    else:
        form = forms.SignUpForm()

    context = {
        "form" : form
    }
    return render(request, "signup.html", context)

def logoutview(request):
    logout(request)
    msg.info(request, "Sorry to see you go :(")
    return redirect('home')

def bookataxi(request):

    if request.POST:
        print(request.POST)
        if request.POST["paymode"] == "Online Payment":
            if request.POST["code"] == "1234567890":
                # pay online success and save
                msg.info(request, "Taxi Booked, Happy journey, Our team will reach out to you soon.")
                saveobj = models.BookingInformation(UserID = request.user, FromLocation = request.POST["FromInput"], ToLocation = request.POST["ToInput"], VehicalType = request.POST["vehicaltype"], PaymentMode = request.POST["paymode"])
                saveobj.save()
            else:
                # pay online failed
                msg.info(request, "<b style='color:red;'>Payment Failed, Please try again</b>")
                return redirect("booktaxi")

        else:
            msg.info(request, "Taxi Booked, Happy journey, Our team will reach out to you soon. OFFLINE")
            saveobj = models.BookingInformation(UserID = request.user, FromLocation = request.POST["FromInput"], ToLocation = request.POST["ToInput"], VehicalType = request.POST["vehicaltype"], PaymentMode = request.POST["paymode"])
            saveobj.save()
        return redirect("booktaxi")
    context = {

    }
    return render(request, "booktaxi.html", context)