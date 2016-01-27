from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Rango says hey there world! <a href='/rango/about'>Click here to find more about me.</a>")


def about(request):
    return HttpResponse("This sentence is about rango! If don't like it here, <a href='/rango'>click this.</a>")
