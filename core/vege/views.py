from django.shortcuts import render, redirect
from vege.models import *

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
    return render (request, 'receipes.html', context = {'page' : 'Receipes', 'receipes' : queryset})

def delete_rec(request, id):
   qdel = rec.objects.get(id = id)
   qdel.delete()
   return redirect('/receipes/')


