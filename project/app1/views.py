from django.shortcuts import render
from app1.forms import userform,userprofileform

# import things for login and logof
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse


# Create your views here.
def index(request):
    return render(request,'app1/index.html')

@login_required
def logout_form(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def special(request):
    return HttpResponse("thanku you are login")


def register(request):
    registered = False

    if request.method == 'POST':
          u = userform(request.POST)
          p = userprofileform(request.POST)
          if u.is_valid() and p.is_valid():
               user = u.save() # form ko database main save kia ar variable main rakha
               user.set_password(user.password) # password ko hasher main convert krna for safety
               user.save() # then passwrod to database main save kia

               profile = p.save(commit=False) # form ko save kia but databse main ni and vaiable main rakh lia
               profile.user = user  # onetoone relationship as it was in model

               if 'portfoliopic' in request.FILES:
                   profile.portfoliopic = request.FILES['portfoliopic']  # agr image form main di gai hai to ose save kr lo

               profile.save() # save this form in databse
               registered = True
          else:
               print(u.errors, p.errors)
    else:
          u = userform()
          p = userprofileform()
    return render(request,'app1/register.html',{'userform':u,'userprofileform':p,'registered':registered})

def login_form(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password = password) # built-in django func for checking if user and pass are match in database
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("USER IS UNACTIVE")

        else:
            print("someone tried to login")
            print("username {} and password {}".format(username,password))
            return HttpResponse("invalid details are given")

    else:
        return render(request,'app1/login.html',{})
