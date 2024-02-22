from django.urls import path
from admissions import views

urlpatterns=[
    path('createadmission/',views.admissions1)
]