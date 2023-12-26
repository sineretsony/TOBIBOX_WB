from django.contrib.auth import logout, login
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .forms import RegistrationForm
from .models import ContactsInfo, AboutInfo, IndexPost, UserProfile, \
    CarouselImg


# Create your views here.
def index(request):
    posts = IndexPost.objects.all().order_by('-published_date')
    carousel = CarouselImg.objects.first()
    context = {'posts': posts, 'carousel': carousel}
    return render(request, 'TOBIBOX/index.html', context=context)


def contacts(request):
    info = ContactsInfo.objects.all()
    context = {'info': info}
    return render(request, 'TOBIBOX/contacts.html', context=context)


def about(request):
    info = AboutInfo.objects.all()
    context = {'info': info}
    return render(request, 'TOBIBOX/about.html', context=context)


def post(request, id=None):
    info = get_object_or_404(IndexPost, post_title=id)
    context = {'info': info}
    return render(request, 'TOBIBOX/post.html', context=context)


def constructor(request):
    return render(request, 'TOBIBOX/index.html')


def profile(request):
    try:
        user_profile = User.objects.get(username=request.user)
        context = {'user': user_profile }
        return render(request, 'TOBIBOX/profile.html', context=context)
    except:
        return HttpResponseRedirect('/login')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            UserProfile.objects.create(user=user)
            return redirect('index')
    else:
        form = RegistrationForm()

    return render(request, 'TOBIBOX/register.html', {'user_form': form})

