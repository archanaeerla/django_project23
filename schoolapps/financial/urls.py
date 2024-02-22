from django.urls import path
from admissions.views import finance1
from admissions.views import finance2


urlpatterns=[
    path('paybill/',finance1),
    path('viewbill/',finance2),
]