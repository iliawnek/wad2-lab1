from string import *

from django.shortcuts import render
from django.http import HttpResponse
from rango.models import *
from rango.forms import *


def index(request):
    context_dict = {}

    category_list_likes = Category.objects.order_by('-likes')#[:5]
    context_dict['categories_by_likes'] = category_list_likes
    category_list_views = Category.objects.order_by('-views')#[:5]
    context_dict['categories_by_views'] = category_list_views

    return render(request, 'rango/index.html', context_dict)


def about(request):
    return render(request, 'rango/about.html')


def category(request, category_name_slug):
    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)
        context_dict['category'] = category
        context_dict['category_name'] = category.name

        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages

    except Category.DoesNotExist:
        pass

    return render(request, 'rango/category.html', context_dict)


def add_category(request):
    context_dict = {}

    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print form.errors

    else:
        form = CategoryForm()

    context_dict['form'] = form
    return render(request, 'rango/add_category.html', context_dict)
