from django.shortcuts import render
from django.http import HttpResponseRedirect, request,response,HttpResponse,HttpResponseBadRequest
from django.urls import reverse
from .models import * 
# Create your views here.
def index(request):
    return render(request,'index.html',{
        'flights':Flight.objects.all()
    })
    
def flight(request,fligth_id):
    try:
        flight=Flight.objects.get(pk=fligth_id)
        
        return render(request,"flight.html",{
                'flight':flight,
                'passengers':flight.passengers.all(),
                'nonpassengers':Passenger.objects.exclude(flights=flight).all()
            })
       
    except Flight.DoesNotExist:
        return render(request,"flight.html",{
            'error_message':"Flight Does Not Found"
        })
def book(request, flight_id):
    if request.method == 'POST':
        flight = Flight.objects.get(pk=flight_id)
        # Remova a conversão para int() aqui
        passenger = Passenger.objects.get(pk=request.POST['passenger'])
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse('flight', args=(flight_id,)))
    else:
        return HttpResponseBadRequest(request)