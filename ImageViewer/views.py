from django.http import HttpResponse
from django.shortcuts import render, redirect

from myapp.models import *


def about_us(request):
    return render(request,"about.html",{})
def show_home_page(request):
    cats=Category.objects.all()
    images=Image.objects.all()
    data={'images':images,'cats': cats}

    return render(request,"home.html",data)

def show_category_page(request,cid):

    cats=Category.objects.all()
    category=Category.objects.get(pk=cid)


    images=Image.objects.filter(cat=category)
    data={'images':images,'cats': cats}

    return render(request,"home.html",data)

def home(request):
    return redirect('/home')