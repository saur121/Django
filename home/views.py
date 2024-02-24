from django.shortcuts import render, HttpResponse
from home.models import Contact


# Create your views here.

def index(request):
    context = {'name': 'Harry', 'course': 'Django'}
    return render(request, 'home.html', context)
    # return HttpResponse("Let's Go For Food")

def about(request):
    return render(request, 'about.html')
    #return HttpResponse("This is my about page")

def projects(request):
    return render(request, 'projects.html')
    #return HttpResponse("This is my projects page")

def contact(request):
    if request.method == "POST":
        print("This is post")
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        print(name, email, phone)
        contact = Contact(name = name, email = email, phone = phone, desc= desc)
        contact.save()
        print("The  Data has been saved")
          
    return render(request, 'contact.html')
    #return HttpResponse("This is my contact page")
