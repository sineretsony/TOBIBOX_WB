from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponseRedirect, HttpResponse, FileResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
# from . import creating_drawing as create_draw
import creating_drawing as create_draw
from .forms import RegistrationForm
from .models import ContactsInfo, AboutInfo, IndexPost, UserProfile, \
    CarouselImg, DrawTemplates, SocialMedia, BoxCategory
from django.db.models.functions import Lower
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy


# Create your views here.
def returnSocialMedia():
    link = SocialMedia.objects.all()
    return {'links': link}


def getCategory():
    categories = BoxCategory.objects.all()
    return {'categories': categories}


def index(request):
    posts = IndexPost.objects.all().order_by('-published_date')
    carousel = CarouselImg.objects.first()
    context = {'posts': posts, 'carousel': carousel}
    context.update(returnSocialMedia())
    return render(request, 'TOBIBOX/index.html', context=context)


def contacts(request):
    info = ContactsInfo.objects.all()
    context = {'info': info}
    context.update(returnSocialMedia())
    return render(request, 'TOBIBOX/contacts.html', context=context)


def about(request):
    info = AboutInfo.objects.all()
    context = {'info': info}
    context.update(returnSocialMedia())
    return render(request, 'TOBIBOX/about.html', context=context)


def post(request, id=None):
    info = get_object_or_404(IndexPost, post_title=id)
    context = {'info': info}
    context.update(returnSocialMedia())
    return render(request, 'TOBIBOX/post.html', context=context)

def constructor(request):
    templates_drawing = DrawTemplates.objects.all()
    selected_category = request.GET.get('category', None)
    search_query = request.GET.get('search', None)

    if selected_category:
        templates_drawing = templates_drawing.filter(category__id=selected_category)

    if search_query:
        search_query = search_query.strip().capitalize()
        templates_drawing = templates_drawing.filter(
            Q(draw_name__icontains=search_query) |
            Q(draw_name__icontains=search_query.lower()))

    context = {'info': templates_drawing}
    context.update(returnSocialMedia())
    context.update(getCategory())
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
    context.update(returnSocialMedia())
    return render(request, 'TOBIBOX/draw.html', context=context)


@login_required
def profile(request):
    try:
        user_profile = User.objects.get(username=request.user)
        if request.method == 'POST':
            user_profile.last_name = request.POST.get('last_name')
            user_profile.first_name = request.POST.get('first_name')
            user_profile.save()

        context = {'user': user_profile}
        context.update(returnSocialMedia())
        return render(request, 'TOBIBOX/profile.html', context=context)
    except User.DoesNotExist:
        return HttpResponseRedirect('/login')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login')



class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    success_url = reverse_lazy('profile')


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
    context = {'user_form': form}
    context.update(returnSocialMedia())

    return render(request, 'TOBIBOX/register.html', context=context)


# def invalid_path(request, invalid_path):
#     return render(request, 'TOBIBOX/invalid_path.html', {'invalid_path': invalid_path})

def invalid_path(request, invalid_path):
    context = {'invalid_path': invalid_path}
    context.update(returnSocialMedia())
    return render(request, 'TOBIBOX/invalid_path.html', context=context)
