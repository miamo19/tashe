from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import FomulaireTache
from .models import Tache

# Create your views here.

def index(request):
    
    item_list = Tache.objects.order_by("-date")
    if request.method == "POST":
        form = FomulaireTache(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tache')
    form = FomulaireTache()
    
    page = {
        "forms": form,
        "list": item_list,
        "titre": "La Liste des Taches"
    }
    return render(request, "index.html", page)


def remove(request, item_id):
    item = Tache.objects.get(id=item_id)
    item.delete()
    messages.info(request, "la taches a été suprimé avec succès")
    return redirect('tache')


        
