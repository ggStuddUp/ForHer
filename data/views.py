from django.shortcuts import render
from .models import DataCenter

def index(request):
    data_list = DataCenter.objects.all()
    return render(request, 'data/index.html', context={'data_list': data_list})

