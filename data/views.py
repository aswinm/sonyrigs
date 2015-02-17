from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponseRedirect,HttpResponse
from data.models import Category,Product

def index(request):
    return render(request,"index.html",{'page_title':'Sony Borewells'})

def gallery(request):
    return render(request,"gallery.html",{'page_title':'Gallery | Sony Borewells'})

def sendmail(request):
    if request.method == "POST":
        det = request.POST
        msg = "NAME: " + det["name"]+"\n"
        msg += "EMAIL: "+det["email"]+"\n"
        msg += "Contact Number: "+det["contact"]+"\n"
        msg += "SUBJECT: "+det["subject"]+"\n"
        msg += "MESSAGE: "+det["message"]+"\n"
        s = send_mail(det["subject"],msg,settings.EMAIL_HOST_USER,['sonyrigsmail@gmail.com'])
        if s:
            return HttpResponseRedirect("/?submit=True")
        else:
            return HttpResponseRedirect("/?submit=False")
    else:
        return HttpResponseRedirect("/")

def products(request,cid):

    c = Category.objects.filter(url=cid).first()
    if not c:
        return HttpResponseRedirect('/')
    

    p = Product.objects.filter(cat__url=cid)

    x = Product.objects.all()
    prod_list = {}
    prod_list["waterwellrigs"] = x.filter(cat__url="waterwellrigs")
    prod_list["miningexplorationrigs"] = x.filter(cat__url="miningexplorationrigs")
    if p.count()>4:
        p_li = [p[:4],p[4:]]
    else:
        p_li = [p]
    return render(request,"products_list.html",{'page_title': c.name,'product_list':p,'p_li':p_li,'prod_list':prod_list})

def product(request,pid):
    
    p = Product.objects.filter(url=pid).first()
    x = Product.objects.all()
    prod_list = {}
    prod_list["waterwellrigs"] = x.filter(cat__url="waterwellrigs")
    prod_list["miningexplorationrigs"] = x.filter(cat__url="miningexplorationrigs")
    if not p:
        return HttpResponseRedirect("/")
    table_data = []
    for i in p.desc.split(";"):
        x = {}
        x["name"],x["data"] = i.split(":")
        table_data.append(x)

    return render(request,"product.html",{'prod':p,"content":table_data,'page_title':p.name,'prod_list':prod_list})


def accessories(request):
    return render(request,"accessories.html",{'page_title':"Accessories"})

def services(request):
    return render(request,"services.html",{'page_title':"Services"})

def about(request):
    return render(request,"about.html",{'page_title':"About Us"})

def contact(request):
    return render(request,"contact.html",{'page_title':"Contact Us"})
# Create your views here.
