from django.shortcuts import render
from .models import taskDB

# Create your views here.
def home(request):
    all_items =taskDB.objects.all()

    return render(request, 'index.html', {'all_items':all_items})

