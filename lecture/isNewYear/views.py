from django.shortcuts import render
import datetime

def index(request):
    return render(request,"index.html",{
        "isNewYear":(datetime.datetime.now().day==1 and datetime.datetime.now().month==1)
    })