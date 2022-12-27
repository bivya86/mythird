from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def chai(request):
    return HttpResponse('Happyness is a cup full of Chai')