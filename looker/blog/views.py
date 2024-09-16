from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView
from django.utils import timezone

from .forms import OutfitForm, ClothesItemForm
from .models import Outfit, ClothesItem


User = get_user_model()
# class HomePage(ListView):


def home_page(request):
    template = 'blog/homepage.html'
    return render(request, template)


def outfit_create(request):
    template = 'blog/testform.html'
    form = OutfitForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.author = User.objects.get(pk=1)
            if not form.instance.publication_date:
                form.instance.publication_date = timezone.now()
            form.save()
            return redirect('blog:edit', form.instance.pk)
    context = {
        'form': form,
    }
    return render(request, template, context)


def outfit_edit(request, outfit_id):
    template = 'blog/edit_outfit.html'
    instance = get_object_or_404(Outfit, pk=outfit_id)
    form = OutfitForm(request.POST or None, instance=instance)
    if request.htmx:
        template = 'includes/full_edit_outfit.html'
    if request.method == 'POST':
        template = 'includes/edit_outfit_form.html'
        if form.is_valid():
            form.save()
    context = {
        'form': form,
        'outfit': instance
    }
    return render(request, template, context)


def clothes_create(request, outfit_id):
    outfit = get_object_or_404(Outfit, pk=outfit_id)
    form = ClothesItemForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.outfit = outfit
            form.save()
            return redirect('blog:clothes-detail', form.instance.pk)
        else:
            context = {
                'form': form,
                'outfit_id': outfit_id
            }
            return render(request, 'includes/clothes_form.html', context)


def outfit_edit_clothes_detail(request, clothes_id):
    template = 'includes/clothes_detail.html'
    clothes = get_object_or_404(ClothesItem, pk=clothes_id)
    context = {
        'clothes': clothes
    }
    return render(request, template, context)


def clothes_create_form(request, outfit_id):
    template = 'includes/clothes_form.html'
    context = {
        'form': ClothesItemForm(),
        'outfit_id': outfit_id
    }
    return render(request, template, context)
