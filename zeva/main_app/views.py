from django.shortcuts import render
from .models import Menu,Collection,Customer,Follower


# Create your views here.

def index(request):
    if request.method == 'GET':
        mobj = Menu.objects.all()
        return render(request, "index.html", {'menu': mobj})
    elif request.method == 'POST':
        if request.POST.get("fname") and request.POST.get("email"):
            name = request.POST["fname"]
            email = request.POST["email"]
            sobj = Follower()
            sobj.name = name
            sobj.email = email
            sobj.save()
            mobj = Menu.objects.all()
            cobj = Collection.objects.all()
            return render(request, 'thankyou.html', {'menu': mobj,'colls':cobj})


def display(request,title):

    menu = Menu.objects.all()
    mobj = Menu.objects.get(category=title)
    cobj = Collection.objects.filter(menu=title)
    return render(request,"display.html", {'colls': cobj,'heading': mobj.title,'menu':menu})

def fs(request,id):

    mobj = Menu.objects.all()
    cobj = Collection.objects.get(id=id)
    return render(request, "fs.html", {'menu': mobj,'image':cobj.image})

def fsc(request,id):

    mobj = Menu.objects.all()
    cobj = Customer.objects.get(id=id)
    return render(request, "fsc.html", {'menu': mobj,'image':cobj.image })

def aboutus(request):

    mobj = Menu.objects.all()
    return render(request, "aboutus.html", {'menu': mobj})

def cdiary(request):

    mobj = Menu.objects.all()
    cobj = Customer.objects.all()
    return render(request, "cdiary.html", {'menu': mobj,'clients':cobj})

def faqs(request):

    mobj = Menu.objects.all()
    return render(request, "faqs.html", {'menu': mobj})

def cp(request):

    mobj = Menu.objects.all()
    return render(request, "cp.html", {'menu': mobj})

def tnc(request):

    mobj = Menu.objects.all()
    return render(request, "tnc.html", {'menu': mobj})
