from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponseRedirect

def index(request):
    return render(request,"index.html",{'page_title':'Sony Borewells'})

def sendmail(request):
    if request.method == "POST":
        det = request.POST
        msg = "NAME: " + det["name"]+"\n"
        msg += "EMAIL: "+det["email"]+"\n"
        msg += "SUBJECT: "+det["subject"]+"\n"
        msg += "MESSAGE: "+det["message"]+"\n"
        s = send_mail(det["subject"],msg,settings.EMAIL_HOST_USER,['sonyrigsmail@gmail.com'])
        if s:
            return HttpResponseRedirect("/?submit=True")
        else:
            return HttpResponseRedirect("/?submit=False")
    else:
        return HttpResponseRedirect("/")




# Create your views here.
