from string import *

from datetime import datetime
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from rango.models import *
from rango.forms import *


def index(request):
    # getting popular categories
    context_dict = {}
    category_list_likes = Category.objects.order_by('-likes')#[:5]
    context_dict['categories_by_likes'] = category_list_likes
    category_list_views = Category.objects.order_by('-views')#[:5]
    context_dict['categories_by_views'] = category_list_views

    visits = request.session.get('visits', 1)
    context_dict['visits'] = visits

    reset_last_visit_time = True

    last_visit = request.session.get('last_visit')
    if last_visit:
        last_visit_time = datetime.strptime(last_visit[:-7], "%Y-%m-%d %H:%M:%S")

        if (datetime.now() - last_visit_time).seconds > 3:
            visits += 1
        else:
            reset_last_visit_time = False

    if reset_last_visit_time:
        request.session['last_visit'] = str(datetime.now())
        request.session['visits'] = visits

    response = render(request, 'rango/index.html', context_dict)

    return response


def about(request):
    context_dict = {}

    visits = request.session.get('visits', 0)
    if visits is not 1:
        context_dict['is_plural'] = True

    context_dict['visits'] = visits

    return render(request, 'rango/about.html', context_dict)


def category(request, category_name_slug):
    context_dict = {'slug': category_name_slug}

    try:
        category = Category.objects.get(slug=category_name_slug)
        context_dict['category'] = category
        context_dict['category_name'] = category.name

        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages

    except Category.DoesNotExist:
        pass

    return render(request, 'rango/category.html', context_dict)


@login_required()
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


@login_required()
def add_page(request, category_name_slug):
    context_dict = {'slug': category_name_slug}

    try:
        # adds category related info to context_dict
        category_object = Category.objects.get(slug=category_name_slug)
        context_dict['category'] = category_object
        context_dict['category_name'] = category_object.name

        # handles form
        if request.method == 'POST':
            form = PageForm(request.POST)

            if form.is_valid():
                page = form.save(commit=False)
                page.category = category_object
                page.save()
                return category(request, category_name_slug)
            else:
                print form.errors

        else:
            form = PageForm()

        context_dict['form'] = form

    except Category.DoesNotExist:
        pass

    return render(request, 'rango/add_page.html', context_dict)


def register(request):
    context_dict = {}

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()

            registered = True
        else:
            print user_form.errors, profile_form.errors

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    context_dict['user_form'] = user_form
    context_dict['profile_form'] = profile_form
    context_dict['registered'] = registered

    return render(request, 'rango/register.html', context_dict)


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/rango/')
            else:
                return HttpResponse('Your account has been disabled due to inactivity.')
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Account does not exist.")

    else:
        return render(request, 'rango/login.html', {})


@login_required()
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/rango/')
