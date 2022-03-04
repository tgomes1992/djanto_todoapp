from django.shortcuts import render
from django.http import HttpRequest , HttpResponse ,request

# Create your views here.


def home(request):
    return render(request,"base.html")

