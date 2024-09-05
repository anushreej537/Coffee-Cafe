from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.contrib import messages

def index(request):
    coffee_obj = Coffee.objects.all()
    return render(request,'base.html',{'coffee_obj':coffee_obj})


def createuser(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        coffee = request.POST['coffee']
        coffee_id = Coffee.objects.get(id=coffee)
        if User.objects.filter(email = email).exists():
            messages.error(request,'email already exist')
            return render(request,'base.html')
        else:
            User.objects.create(name=name, email=email, coffee=coffee_id)
            return render(request,'home.html')
    else:
        return render(request,'base.html')

def showuser(request):
    user_obj = User.objects.all()
    print(user_obj)
    return render(request,'home.html',{'user_obj':user_obj})
