from django.shortcuts import render, HttpResponse

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
    return render(request, 'contact.html')
    #return HttpResponse("This is my contact page")
