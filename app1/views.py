from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets

# Create your views here.
def f1(request):
    return HttpResponse("<h1>Paras Gupta</h1>")

class Auth(viewsets.ViewSet):
    def create(self,request):
        return HttpResponse("<div style= 'margin: 50px 50px'>nalayak</div>")