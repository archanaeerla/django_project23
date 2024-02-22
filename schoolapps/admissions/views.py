from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def admission1(request):
    return HttpResponse("this is my first admission page")

def admission2(request):
    return HttpResponse("this is my second admisssion page")