from django.contrib.auth import logout, login
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse, FileResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from . import creating_drawing as create_draw
from .forms import RegistrationForm
from .models import ContactsInfo, AboutInfo, IndexPost, UserProfile, CarouselImg, DrawTemplates



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
    templates_drawing = DrawTemplates.objects.all()
    context = {'info': templates_drawing}
    return render(request, 'TOBIBOX/constructor.html', context=context)


def draw(request, id=None):
    info = get_object_or_404(DrawTemplates, draw_name=id)
    if request.method == 'POST':
        name_templates_draw = str(request.POST.get('name_templates_draw'))
        width = int(request.POST.get('width'))
        height = int(request.POST.get('height'))
        depth = int(request.POST.get('depth'))
        material = int(request.POST.get('material'))
        new_draw = create_draw.create_svg_document(width, height, depth, material, name_templates_draw)
        response = FileResponse(open(new_draw, 'rb'), filename=name_templates_draw)
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(f'{name_templates_draw}_{width}x{height}x{depth}mm.svg')
        return response
    context = {'info': info}
    return render(request, 'TOBIBOX/draw.html', context=context)


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

