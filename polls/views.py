from django.http import HttpResponse
from django.shortcuts import render
from polls.models import Con
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.template import loader


def index(request):
    return render(request,'index.html')

def con(request):
    if request.method == "POST":
        email = request.POST.get('email')
        pwd = request.POST.get('pwd')
        con = Con(email=email, pwd=pwd)
        con.save()
        messages.success(request, 'Submit success fully !')
    return render(request,'contect.html')
        

def about(request):
    return render(request,'about.html')

def signin(request):
    # if request.method == "POST":
    #     username = request.POST['username']
    #     password = request.POST['username']
    #     user = authenticate(username=username,password=password)
    #     if user is not None:
    #         login(request,user)
    #         messages.success(request,'success fully login !!!!!')

    
    return render(request,'authenticate/signin.html')

def signup(request):
    return render(request,'authenticate/signup.html')

# def testing(request):
#   mydata = con.Object.all().values()
#   template = loader.get_template('/')
#   context = {
#     'mymembers': mydata,
#   }
#   return HttpResponse(template.render(context, request))