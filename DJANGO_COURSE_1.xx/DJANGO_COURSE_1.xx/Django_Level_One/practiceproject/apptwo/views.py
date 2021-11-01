from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<em>My Second App<em>")

def help(request):
    dict = {'insert_help':'Hello I am from views.py help.html'}
    return render(request, 'apptwo/help.html', context=dict)
