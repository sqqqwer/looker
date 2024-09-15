from django.urls import path

from . import views


app_name = 'blog'

urlpatterns = [
    # path('', views.HomePage.as_view(), name='homepage'),
    path('', views.home_page, name='homepage'),
    # path('outfit/create', views.OutfitCreate.as_view(), name='create'),
    path('outfit/create', views.outfit_create, name='create'),
    path('outfit/<int:outfit_id>/edit', views.outfit_edit, name='edit'),
    path('htmx/clothes/<int:clothes_id>/detail',
         views.outfit_edit_clothes_detail,
         name='clothes-detail'),
    path('htmx/outfit/<int:outfit_id>/clothes/create_form/',
         views.clothes_create_form,
         name='clothes-create-form'),
    path('htmx/outfit/<int:outfit_id>/clothes/create/',
         views.clothes_create,
         name='clothes-create'),
    # path('outfit/<int:outfit_id>', views.OutfitDetail.as_view(), name='detail'),
    # path('outfit/<int:outfit_id>/delete', views.OutfitDelete.as_view(), name='delete'),
]
