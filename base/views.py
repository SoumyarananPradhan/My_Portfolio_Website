from django.shortcuts import render
from django.contrib import messages
from base import models
from base.models import contact

# Create your views here.

def contact(req):
    if req.method =="POST":
        print('post')
        name = req.POST.get('name')
        email = req.POST.get('email')
        number = req.POST.get('number')
        content = req.POST.get('content')
        print(name,email,number,content)

        if len(name) > 1 and len(name) < 30:
            pass
        else:
            messages.error(req, 'Length of Name should be greater than 2 and less than 30')
            return render(req, 'base/home.html')

        if len(email) > 1 and len(name) < 30:
            pass
        else:
            messages.error(req, 'Length of Email should be greater than 2 and less than 30')
            return render(req, 'base/home.html')

        if len(number) >= 10 and len(number) < 13:
            pass
        else:
            messages.error(req, 'Invalid Number,Try Again!')
            return render(req, 'base/home.html')

        ins = models.contact(name=name,email=email,number=number,content=content)
        ins.save()
        messages.success(req, 'Thank You For Contacting Me. Your message have been saved.')
        print('Data has been saved to database...')
        print('the request is no pass')
    
    return render(req, 'base/home.html')

