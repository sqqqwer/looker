from django.contrib.auth import get_user_model
from django.http import Http404
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone


import time

User = get_user_model()
# class HomePage(ListView):


# def home_page(request):
#     template = 'blog/homepage.html'
#     return render(request, template)


# def outfit_create(request):
#     template = 'blog/testform.html'
#     form = OutfitForm(request.POST or None)
#     if request.method == 'POST':
#         if form.is_valid():
#             form.instance.author = User.objects.get(pk=1)
#             if not form.instance.publication_date:
#                 form.instance.publication_date = timezone.now()
#             form.save()
#             return redirect('blog:edit', form.instance.pk)
#     context = {
#         'form': form,
#     }
#     return render(request, template, context)


# def outfit_edit(request, outfit_id):
#     template = 'blog/edit_outfit.html'
#     outfit = get_object_or_404(Outfit, pk=outfit_id)
#     clothes_list = outfit.clothes.all()
#     form = OutfitForm(request.POST or None, instance=outfit)
#     if request.htmx:
#         template = 'includes/full_edit_outfit.html'
#     if request.method == 'POST':
#         template = 'includes/edit_outfit_form.html'
#         if form.is_valid():
#             form.save()
#     context = {
#         'form': form,
#         'outfit': outfit,
#         'clothes_list': clothes_list
#     }
#     return render(request, template, context)


# def outfit_edit_clothes_detail(request, clothes_id):
#     if not request.htmx:
#         raise Http404('Page Not Found')
#     # тут проверяется есть ли ссылка на картинку 
#     # если ссылки нет то парсится (в это время показывается тэмплейт с загрузкой)

#     # парсится асинхронно чтобы паралельно можно было создавать другие вещи
#     # ИЛИ сделать загрузку сплошной и парсинг сделать в одноканале
#     template = 'includes/clothes_detail.html'
#     clothes = get_object_or_404(ClothesItem, pk=clothes_id)
#     context = {
#         'clothes': clothes,
#     }
#     return render(request, template, context)


# def clothes_loading_image(request, clothes_id):
#     template = 'includes/clothes_loading.html'
#     clothes = get_object_or_404(ClothesItem, pk=clothes_id)
#     context = {
#         'clothes': clothes,
#     }
#     return render(request, template, context)



# def clothes_create(request, outfit_id):
#     if not request.htmx:
#         raise Http404('Page Not Found')
#     template = 'includes/clothes_create_form.html'
#     outfit = get_object_or_404(Outfit, pk=outfit_id)
#     form = ClothesItemForm(request.POST or None)

#     if request.method == 'POST':
#         if form.is_valid():
#             form.instance.outfit = outfit
#             form.save()
#             time.sleep(3)
#             # тэмплейт с загрузкой
#             # в тэмпейте с загрузкой запускается тэмплейт детейла
#             return redirect('blog:clothes-detail', form.instance.pk)

#     context = {
#         'form': form,
#         'outfit': outfit
#     }
#     return render(request, template, context)


# def clothes_edit(request, clothes_id):
#     if not request.htmx:
#         raise Http404('Page Not Found')
#     template = 'includes/clothes_edit_form.html'
#     clothes = get_object_or_404(ClothesItem, pk=clothes_id)
#     form = ClothesItemForm(request.POST or None, instance=clothes)

#     if request.method == 'POST':
#         if form.is_valid():
#             form.save()
#             return redirect('blog:clothes-loading-image', form.instance.pk)

#     context = {
#         'form': form
#     }
#     return render(request, template, context)


# def clothes_delete(request, clothes_id):
#     if not request.htmx:
#         raise Http404('Page Not Found')
#     template = 'includes/clothes_delete_quote.html'
#     clothes = get_object_or_404(ClothesItem, pk=clothes_id)
#     form = ClothesItemForm(instance=clothes)
#     if request.method == 'POST':
#         clothes.delete()
#         return HttpResponse('')

#     context = {
#         'form': form,
#     }
#     return render(request, template, context)
