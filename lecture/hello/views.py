from django.shortcuts import render
from django.http import HttpResponse


def index(request,name):
    return render(request,"hello/index.html",{
        "name":name
    })
def smith(request):
        return HttpResponse("Hello Smith")
def greet(request,name):
        return render(request,"hello/greet.html",{
            'name':name})
