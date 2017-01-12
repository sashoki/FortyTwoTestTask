# -*- coding: utf-8 -*-
from django.core.mail import send_mail
from django.http import BadHeaderError
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from forms import HomeForm, ContactForm, MyContactsForm
from apps.hello.models import Home, MyContacts
from django.core.context_processors import csrf
from django.utils import timezone
from django.contrib import auth
from django.contrib.admin.widgets import AdminDateWidget

# Create your views here.


def index(request):
    return render(request, "index.html")

def contacts(request, pk=1):
    args = {}
    args['mycontacts'] = MyContacts.objects.get(pk=pk)
    args['username'] = auth.get_user(request).username
    return render(request, 'contacts.html', args)

def homes(request, page_number=1):
    args = {}
    args['homes'] = Home.objects.all()
    args['username'] = auth.get_user(request).username
    return render(request, 'homes.html', args)


def home(request, pk=1):
    args = {}
    args.update(csrf(request))
    args['home'] = Home.objects.get(pk=pk)
    args['username'] = auth.get_user(request).username
    return render(request, 'home.html', args)

def create(request):
    if request.method == 'POST':
        form = HomeForm(request.POST)
        if form.is_valid():
            home = form.save(commit=False)
            home.home_data = timezone.now()
            home.save()
            return redirect('apps.hello.views.home', pk=home.pk)
    else:
        form = HomeForm()
        args = {}
        args['form'] = form
    return render(request, 'post_edit.html', args)


def post_edit(request, pk):
    home = get_object_or_404(Home, pk=pk)
    args = {}
    args['home'] = home
    if request.method == 'POST':
        form = HomeForm(request.POST, instance=home)
        if form.is_valid():
            home = form.save(commit=False)
            home.home_data = timezone.now()
            home.save()
            return redirect('apps.hello.views.home', pk=home.pk)
    else:
        form = HomeForm(instance=home)
        args['form'] = form
    return render(request, 'post_edit.html', args)



# Функція форми зворотнього звязку
def callback(reguest):
    if reguest.method == 'POST':
        form = ContactForm(reguest.POST)
        # Якщо форма заповнена коректно, зберегти всі введені користувачем значення
        if form.is_valid():
            name = form.cleaned_data['name']
            phon = form.cleaned_data['phon']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            copy = form.cleaned_data['copy']

            recepients = ['sania_piter@mail.ru']
            # Якщо користувач хоче отримати копію собі, додаємо його до списку отримувачів
            if copy:
                recepients.append(email)
            try:
                send_mail(name, phon, message, email, recepients)
            except BadHeaderError: # Захист від вразливості
                return HttpResponse('Invalid header found')
            # Перехід на іншу сторінку, якщо повідомлення відправлено
            return HttpResponseRedirect("/")

    else:
        form = ContactForm()
    # Вивід форми в шаблон
    return render(reguest, 'callback.html', {'form': form, 'username': auth.get_user(reguest).username})


"""def thanks(reguest):
    thanks = 'thanks'
    return render(reguest, 'thanks.html', {'thanks': thanks})"""



def my_edit(request, pk):
    mycontacts = get_object_or_404(MyContacts, pk=pk)
    args = {}
    args['mycontacts'] = mycontacts
    if request.method == 'POST':
        form = MyContactsForm(request.POST, instance=mycontacts)
        if form.is_valid():
            mycontacts = form.save(commit=False)
            #mycontacts.date_of_birth = AdminDateWidget.media()
            mycontacts.save()
            return redirect('/', pk=mycontacts.pk)
    else:
        form = MyContactsForm(instance=mycontacts)
        args['form'] = form
    return render(request, 'my_edit.html', args)