from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .user import User

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def protfolio(request):
    return render(request, 'protfolio.html')

def service(request):
    return render(request, 'service.html')

def contact(request):
    return render(request, 'contact.html')

def thanks(request):
    return render(request, 'thanks.html')

def calculator(request):
    result = ""
    try:
        if request.method == "POST":
            n1 = eval(request.POST.get('value1'))
            n2 = eval(request.POST.get('value2'))
            cal = request.POST.get('cal')
            if cal == "+":
                result = n1+n2
            elif cal == "-":
                result = n1-n2
            elif cal == "*":
                result = n1*n2
            if cal == "/":
                result = n1/n2
        
    except:
        pass
    return render(request, 'calculator.html', {"final": result})

def form(request):
    result = User()
    data = {"form": result}
    return render(request, "form.html", data)
    # try:
    #     if request.method == "POST": 
    #         name=request.POST.get('name')
    #         email=request.POST.get('email')
    #         subject=request.POST.get('subject')
    #         message=request.POST.get('message')
    #         return HttpResponseRedirect("/thanks/")


    #         result = f"{name} {email} {subject} {message}"
    #         data = {
    #             "final": result,
    #             "name": name,
    #             "email": email,
    #             "subject": subject,
    #             "message": message,
    #         }
        
    # except:
    #     pass
      
    # return render(request, "form.html")
# Bdset@1234