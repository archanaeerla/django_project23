from django.shortcuts import render


# Create your views here.
def admission1(request):
    return render(request,'admissions/newadmissions.html')

def admission2(request):
    return render(request,'admissions/oldadmissions.html')