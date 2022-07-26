from distutils.command.build_scripts import first_line_re
from email.mime import application
from django.shortcuts import render
from backend.models import Application

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
    return render(request, "backend/application_form.html", {
        "backend" : Application.objects.all()
    })
def applicant_form(request, pk):
    application = Application.objects.get(pk=pk)
    if request.method == "POST":
        data = request.POST
        first_name = data.get("first_name")
        first_name.save()
    return render(request, "backend/application_form.html")
    
        