from django.shortcuts import render
from backend.models import Application
from django.http import HttpResponseRedirect
from django.urls import reverse
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

def apply(request):
    if request.method == "POST":

        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        applicant_data = Application(first_name=first_name, last_name=last_name)
        applicant_data.save()
    return HttpResponseRedirect(reverse("application_form"))