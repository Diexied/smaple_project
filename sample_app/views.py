from django.shortcuts import render
from .models import Person

def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def form(request):

    if request.method == "POST":

        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")

        Person.objects.create(
            first_name=first_name,
            last_name=last_name
        )

    return render(request, 'form.html', {'message':'Saved Successfully'})