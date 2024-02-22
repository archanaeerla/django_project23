from django.urls import path
from admissions import views

urlpatterns=[
    path('createadmission/',views.admission1),
    path('viewadmission/',views.admission2),
]