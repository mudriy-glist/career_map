from django.shortcuts import render
from django.http import HttpResponse, Http404

# Create your views here.
def index(request):
    return render(request, "backend/index.html")

def mecha(request):
    return render(request, "backend/mecha.html")

def woodoo(request):
    return render(request, "backend/woodoo.html")

def voodoo_newstarter(request):
    return render(request, "backend/voodoo_newstarter.html")

def application_form(request):
    return render(request, "backend/application_form.html")