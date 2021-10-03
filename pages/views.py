from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home_page(req):
    return HttpResponse('Hello World')
