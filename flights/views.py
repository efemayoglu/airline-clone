from django import forms
from django.http import HttpResponseBadRequest, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse

from .models import Flight, FFlight, Passenger
from django.http import JsonResponse
# Create your views here.
from django.core import serializers

from django.http import HttpResponse
import json

def index(request):

    arr = []

    for i in FFlight.objects.all():
        arr.append({'id':i.id, 'name':i.name})
  
    return HttpResponse(json.dumps(arr), content_type="application/json")


    # data = serializers.serialize("json", Flight.objects.all())

    # return HttpResponse(data)

def flight(request, flight_id):
    try:
        flight = Flight.objects.get(id=flight_id)
    except Flight.DoesNotExist:
        raise Http404("Flight not found.")
    return render(request, "flights/flight.html", {
        "flight": flight,
        "passengers": flight.passengers.all(),
        "non_passengers": Passenger.objects.exclude(flights=flight).all()
    })

def book(request, flight_id):
    if request.method == "POST":
        try:
            passenger = Passenger.objects.get(pk=int(request.POST["passenger"]))
            flight = Flight.objects.get(pk=flight_id)
        except KeyError:
            return HttpResponseBadRequest("Bad Request: no flight chosen")
        except Flight.DoesNotExist:
            return HttpResponseBadRequest("Bad Request: flight does not exist")
        except Passenger.DoesNotExist:
            return HttpResponseBadRequest("Bad Request: passenger does not exist")
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse("flights:flight", args=(flight_id,)))
