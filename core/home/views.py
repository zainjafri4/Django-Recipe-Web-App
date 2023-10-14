from django.shortcuts import render
from django.http import HttpResponse

def home(request):    

    peoples =  [
     { 'name' : 'Zain', 'age' : 20 },
     { 'name' : 'Ali', 'age' : 33 },
     { 'name' : 'Osama', 'age' : 36 },
     { 'name' : 'Hamza', 'age' : 41 } ,
     { 'name' : 'Mohsin', 'age' : 16 } ,
     { 'name' : 'Ahmad', 'age' : 14 } ]  

    return render(request, 'index.html', context={'peoples' : peoples, 'page' : 'Home'})

def about(request):
    return render(request, 'about.html', context={'page' : 'About'})

def contact(request):
    return render(request, 'contact.html', context={'page' : 'Contact'})