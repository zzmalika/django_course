from django.shortcuts import render
from datetime import datetime, timedelta
from django.http import HttpResponse
# Create your views here.


def index(request):
    user = {
        'id': '123',
        'username': 'zzmalika',
        'is_authenticated': True
    }
    context = {
        'user': user,
        'status': 1
    }
    return render(request, 'index.html', context=context)


def current_datetime(request):
    return HttpResponse(datetime.now())


def time_plus(request):
    if request.GET['hours']:

        dt = datetime.now() + timedelta(hours=int(request.GET['hours']))
        return HttpResponse(dt)
    else:
        HttpResponse('null')


def hours_ahead(request, **kwargs):
    dt = datetime.now() + timedelta(days=kwargs.get('asd'), hours=kwargs.get('asd1'))
    return HttpResponse(dt)
