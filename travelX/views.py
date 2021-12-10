from django.shortcuts import render
from django.template import Template , Context


# Create your views here.
def index(request):
    return render(request,"index.html")
