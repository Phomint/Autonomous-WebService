from django.shortcuts import render

def index(request):
    return render(request, '../templates/base.html')
# Create your views here.
