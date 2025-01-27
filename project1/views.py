from django.shortcuts import render
from service.models import Service

def home(request):
    serviceData = Service.objects. all().order_by("service_title")[2:]
    data = {
        "serviceData" : serviceData
    }
    return render(request,"index.html",data)