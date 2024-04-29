from django.shortcuts import render,redirect
from django.http import HttpResponse
from app.models import *

# Create your views here.
def index(request):
    return render(request, 'login.html')
def signup(request):
    return render(request, 'signup.html')
def ins(request):
    u=user()
    u.name=request.GET['a1']
    u.username=request.GET['a2']
    u.pwd=request.GET['a3']
    u.conf_pwd=request.GET['a4']
    u.save()
    return redirect("../login")
def dashboard(request):
    return render(request,'dashboard.html')
def class_A(request):
    u = Classes.objects.all()
    return render(request,'class_A.html', {'x':u})
def choose_class(request):
    return redirect('../class_A')
def show(request):
    u=Classes.objects.all()
    return render(request,'show.html',{'x':u})
def dele(request,id):
    u=Classes.objects.get(id=id)
    u.delete()
    return redirect("../show")
def edit(request,id):
    u=Classes.objects.get(id=id)
    return render(request,'attendance.html',{'x':u})
def edcode(request,id):
    u=Classes.objects.get(id=id)
    u.attendance = request.GET['a4']
    u.save()
    return redirect("../class_A")
def login(request):
    return render(request, 'login.html')
def log(request):
    a = request.GET['a1']
    b = request.GET['a2']
    if user.objects.filter(username = a, pwd = b):
        return redirect('../dashboard')
    else:
        return redirect('../login')
def logout(request):
    return render(request,'logout.html')
def status(request):
    u=Classes()
    u.attendance = request.GET['a4']
    u.save()
    return render(request,'class_A.html')
