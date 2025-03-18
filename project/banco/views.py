from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def saludo(requets):
    return HttpResponse("<h1>hola desde banco</h1>")