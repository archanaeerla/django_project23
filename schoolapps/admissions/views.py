from django.shortcuts import render


# Create your views here.

def homepage(request):
    return render(request,'index.html')

def admission1(request):
    values = {'name':'archana','age':23,'address':'vizag'}
    return render(request,'admissions/newadmissions.html')

def admission2(request):
    return render(request,'admissions/oldadmissions.html')