from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def hello(request):
    return HttpResponse("Привет, Мир!",content_type="text/plan", charset='UTF-8')

def home(request):
    return render(request, 'static_handler.html')

