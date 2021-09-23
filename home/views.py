from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
# for message promting when submitting the file
from django.contrib import messages
# HttpResponse => only to send a string "where as" render => is used to deploy templates (HTML)
# Create your views here.
def index(request):
    return render(request, 'index.html')
    #return HttpResponse('this is our home page')


def about(request):
    #return HttpResponse('this is our about page')
    return render(request, 'about.html')

def skills(request):
    #return HttpResponse('this is our services page')
    return render(request, 'skills.html')

def contact(request):
    #return HttpResponse('this is our contacts page')
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent successfully !!!')
    
    return render(request, 'contact.html')
