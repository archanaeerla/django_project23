from django.shortcuts import render
from django.urls import path
from django.http import HttpResponse

# Create your views here.
def admission1(request):
    return HttpResponse("this is first admission page")

def admission2(request):
    return HttpResponse("this is second admission page")