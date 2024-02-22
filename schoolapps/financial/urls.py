from django.urls import path
from financial.views import finance1
from financial.views import finance2


urlpatterns=[
    path('paybill/',finance1),
    path('viewbill/',finance2),
]