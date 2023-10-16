from django.shortcuts import render, redirect
from vege.models import *
from django.contrib.auth.models import User
from django.contrib import messages



def receipes(request):
    if request.method == 'POST':

      rec_data = request.POST
      rec_image = request.FILES.get('rec_image')
      rec_name = rec_data.get('rec_name')
      rec_dec = rec_data.get('rec_dec')
      print(rec_name)
      print(rec_dec)

      rec.objects.create(
         rec_name = rec_name,
         rec_dec = rec_dec,
         rec_image = rec_image,
         
      )
      return redirect('/receipes')
    
    queryset = rec.objects.all()
    
    search = request.GET.get('search')
    if search:
       queryset = queryset.filter(rec_name__icontains = search)
       print (search)

    return render (request, 'receipes.html', context = {'page' : 'Receipes', 'receipes' : queryset})

def delete_rec(request, id):
   qdel = rec.objects.get(id = id)
   qdel.delete()
   return redirect('/receipes/')

def update_rec(request, id):
   qupdate = rec.objects.get(id = id)

   if request.method == 'POST':
      rec_data = request.POST

      rec_image = request.FILES.get('rec_image')
      rec_name = rec_data.get('rec_name')
      rec_dec = rec_data.get('rec_dec')

      qupdate.rec_name = rec_name
      qupdate.rec_dec = rec_dec

      if rec_image:
         qupdate.rec_image = rec_image

      qupdate.save()
      return redirect('/receipes/')

   return render(request, 'update_rec.html', context = {'receipe' : qupdate} ) 


def login(request):
   return render (request, 'login.html')

def register(request):
   if request.method == 'POST':

      user_data = request.POST

      first_name = user_data.get('first_name')
      last_name = user_data.get('last_name')
      username = user_data.get('username')
      password = user_data.get('password')

      print(first_name, last_name, username, password)  

      user = User.objects.filter(username = username)

      if user.exists():
         messages.info(request, "username already exists")
         return redirect ('/register/')

      user1 = User.objects.create(
      first_name=first_name,
      last_name=last_name,
      username=username)
      user1.set_password(password)
      user1.save()

      messages.info(request, "Account Created Successfully")
      return redirect('/register/')
      
      
   return render(request, 'register.html')