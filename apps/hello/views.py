from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from forms import HomeForm
from apps.hello.models import Home
from django.core.context_processors import csrf
from django.utils import timezone

# Create your views here.


def index(request):
    return render(request, "index.html")


def homes(request, page_number=1):
    args = {}
    args['homes'] = Home.objects.all()
    return render(request, 'homes.html', args)


def home(request, pk=1):
    args = {}
    args.update(csrf(request))
    args['home'] = Home.objects.get(pk=pk)
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


def callback(request):
    if request.is_ajax():
        message = "Hello AJAX"
    else:
        message = "Hello"
    return HttpResponse(message)




