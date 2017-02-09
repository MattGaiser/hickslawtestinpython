"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
from django.template import RequestContext
from datetime import datetime
from random import randint
from django.utils.timezone import localtime, now
from app.models import DataPoint
from . import models

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        data = DataPoint()
        data.starttime = datetime.now()
        data.seconds = int(request.GET['starttime'])
        data.endtime = datetime.now()
        data.numOfElements = request.GET['nVal']
    
        if data.endtime.second > data.seconds:
            data.timetaken = data.endtime.second - data.seconds
        else:
            data.timetaken = 60 - data.seconds + data.endtime.second
        data.save()

    entries = DataPoint.objects.order_by('id')

    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
            'entries':entries,
        }
    )

def test(request):
    """Renders the test page."""
    assert isinstance(request, HttpRequest)
    numVar = randint(1,5) * 2
    pizza2var = False
    pizza3var = False
    pizza4var = False
    pizza5var = False
    time = datetime.now()
    timeformatted = datetime.now().strftime('%S')

    if numVar > 2:
        pizza2var = True
    if numVar > 4:
        pizza3var = True
    if numVar > 6:
        pizza4var = True
    if numVar > 8:
        pizza5var = True


    return render(
        request,
        'app/test.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
            'randomNum': numVar,
            'pizza2': pizza2var,
            'pizza3': pizza3var,
            'pizza4': pizza4var,
            'pizza5': pizza5var,
            'time': time,
            'timeformatted':timeformatted,
        }
    )

#def create(request):
    
   