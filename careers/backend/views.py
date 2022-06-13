from django.shortcuts import render
from django.http import HttpResponse, Http404

# Create your views here.
def index(request):
    return render(request, "backend/index.html")

elements = ["backend/button.html",
        "TEST 2 lalalallwrqk12r12fwqsdqwql21l,12,r",
        "TEST 3 lalalallwrqk12r12fwasdq111fffffffasd"]

def section(request, num):
    if 1 <= num <= 3:
        return render(request, elements[num - 1])
    else:
        raise Http404("No such section")