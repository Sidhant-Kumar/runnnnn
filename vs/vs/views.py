from django.http import HttpResponse
from django.shortcuts import render


def idd(request, id):
    return HttpResponse('<b>' + id + '</b>')


def home(request):
    data = {
        'title':'hmmmm',
        'work': 'i think it is working',
    }
    return render(request, 'index.html',data)
