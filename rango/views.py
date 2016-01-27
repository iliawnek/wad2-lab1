from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context_dict = {'boldmessage': "I am bold."}
    return render(request, 'rango/index.html', context_dict)


def about(request):
    return HttpResponse("This sentence is about rango! If you don't like it here, <a href='/rango'>click this.</a>")
