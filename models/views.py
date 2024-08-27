from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404

from .bot import get_post
from .models import Leeds, Status, called
from .forms import LeedsForm, LeedsFormUpdateForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

@login_required
def home_page(request):
    leeds = Leeds.objects.all().order_by('-create_time')
    page = request.GET.get('page', 1)

    paginator = Paginator(leeds, 20)
    try:
        pages = paginator.page(page)
    except PageNotAnInteger:
        pages = paginator.page(1)
    except EmptyPage:
        pages = paginator.page(paginator.num_pages)
    context = {
        "pages": pages,
    }
    return render(request, 'index.html', context)


def contact_page(request):
    # form = LeedsForm(request.POST or None)
    if request.method == 'POST':
        form = LeedsForm(request.POST or None)
        name = request.POST.get('name')
        phonenumber = request.POST.get('phonenumber')
        Leeds.objects.create(
            name=name,
            phonenumber=phonenumber,
        )
        get_post(form.data)
        return redirect('success')
    return render(request, 'form.html', {})



def success(req):
    return render(req, 'success.html', {})
def success_logout(req):
    return render(req, 'success_logout.html', {})
@login_required
def SinglePageView(request, slug):
    post = get_object_or_404(Leeds, id=slug)

    if request.method == 'POST':
        form = LeedsFormUpdateForm(request.POST, instance=post)
        if form.is_valid():
            print(23456)

            updated_post = form.save(commit=False)
            updated_post.author = request.user
            updated_post.save()
            return redirect('single', slug=post.id)
    else:
        form = LeedsForm()
    context = {
        "post": post,
        'statuss': Status,
        'form': form,
    }
    # print(post.status.split("'")[1])
    return render(request, 'single.html', context)

@login_required
def called_page(request):
    leeds = Leeds.objects.filter(status='called').order_by('-create_time')
    page = request.GET.get('page', 1)

    paginator = Paginator(leeds, 20)
    try:
        pages = paginator.page(page)
    except PageNotAnInteger:
        pages = paginator.page(1)
    except EmptyPage:
        pages = paginator.page(paginator.num_pages)
    context = {
        "pages": pages,
    }
    return render(request, 'called.html', context)




@login_required
def uncalled_page(request):
    leeds = Leeds.objects.filter(status='uncalled').order_by('-create_time')
    page = request.GET.get('page', 1)

    paginator = Paginator(leeds, 20)
    try:
        pages = paginator.page(page)
    except PageNotAnInteger:
        pages = paginator.page(1)
    except EmptyPage:
        pages = paginator.page(paginator.num_pages)
    context = {
        "pages": pages,
    }
    return render(request, 'uncalled.html', context)


@login_required
def recalled_page(request):
    leeds = Leeds.objects.filter(status='recalled').order_by('-create_time')
    page = request.GET.get('page', 1)

    paginator = Paginator(leeds, 20)
    try:
        pages = paginator.page(page)
    except PageNotAnInteger:
        pages = paginator.page(1)
    except EmptyPage:
        pages = paginator.page(paginator.num_pages)
    context = {
        "pages": pages,
    }
    return render(request, 'recalled.html', context)


@login_required
def rejected_page(request):
    leeds = Leeds.objects.filter(status='rejected').order_by('-create_time')
    page = request.GET.get('page', 1)

    paginator = Paginator(leeds, 20)
    try:
        pages = paginator.page(page)
    except PageNotAnInteger:
        pages = paginator.page(1)
    except EmptyPage:
        pages = paginator.page(paginator.num_pages)
    context = {
        "pages": pages,
    }
    return render(request, 'rejected.html', context)

@login_required
def complete_page(request):
    leeds = Leeds.objects.filter(status='complete').order_by('-create_time')
    page = request.GET.get('page', 1)

    paginator = Paginator(leeds, 20)
    try:
        pages = paginator.page(page)
    except PageNotAnInteger:
        pages = paginator.page(1)
    except EmptyPage:
        pages = paginator.page(paginator.num_pages)
    context = {
        "pages": pages,
    }
    return render(request, 'complete.html', context)



def LoginPageView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('login')
    return render(request, 'login.html', {})


def LogoutPageView(request):
    logout(request)
    return redirect('success_logout')