import uuid

from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

from .models import *
# Create your views here.
def login(request, *args, **kwargs):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        name = request.POST.get('name')
        pwd = request.POST.get('pwd')
        try:
            obj = User.objects.get(name=name, pwd=pwd)
            uid = str(uuid.uuid4())
            obj.uid = uid
            obj.save()
            return redirect('/index/')
        except Exception as e:
            return redirect('/login/')

    else:
        pass


def index(request, *args, **kwargs):
    if request.method == 'GET':
        return render(request, 'index.html')

def gen_image(request, *args, **kwargs):
    pass