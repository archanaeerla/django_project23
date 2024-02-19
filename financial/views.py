from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def finance1(request):
    return HttpResponse("this is first financial page")

def finance2(request):
    return HttpResponse("this is second financial page")