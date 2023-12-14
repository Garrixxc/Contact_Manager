from django.shortcuts import redirect, render
from .models import Member

def index(request):
    mem=Member.objects.all()
    return render(request,'index.html',{'mem':mem})

def add(request):
    return render(request,'add.html')

def repeatName(request):
    return render(request,'repeatName.html')

def addrec(request):
    x=request.POST['first']
    y=request.POST['num']
    z=request.POST['email']
    n=request.POST['notes']
    if Member.objects.exists():
        if Member.objects.filter(firstname=x).exists():
            return render(request, 'repeatName.html', {'error_message': 'Name already exists!'}, status=400)
    mem=Member(firstname=x,num=y,email=z, notes=n)
    mem.save()
    return redirect("/")

def delete(request,id):
    mem=Member.objects.get(id=id)
    return render(request,'delete.html',{'mem':mem})

def confirm_delete(request,id):
    mem=Member.objects.get(id=id)
    mem.delete()
    return redirect("/")

def update(request,id):
    mem=Member.objects.get(id=id)
    return render(request,'update.html',{'mem':mem})

def contact(request,id):
    mem=Member.objects.get(id=id)
    return render(request,'contact.html',{'mem':mem})

def uprec(request,id):
    x=request.POST['first']
    y=request.POST['num']
    z=request.POST['email']
    n=request.POST['notes']
    mem=Member.objects.get(id=id)
    mem.firstname=x
    mem.num=y
    mem.email=z
    mem.notes=n
    mem.save()
    return redirect("/")
