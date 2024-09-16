from django.urls import path

from . import views


app_name = 'blog'

urlpatterns = [
    # path('', views.HomePage.as_view(), name='homepage'),
    path('', views.home_page, name='homepage'),
    # path('outfit/create', views.OutfitCreate.as_view(), name='create'),
    path('outfit/create', views.outfit_create, name='create'),
    path('outfit/<int:outfit_id>/edit', views.outfit_edit, name='edit'),
    path('htmx/outfit/<int:outfit_id>/clothes/create/',
         views.clothes_create,
         name='clothes-create'),
    path('htmx/clothes/<int:clothes_id>/detail',
         views.outfit_edit_clothes_detail,
         name='clothes-detail'),
    path('htmx/clothes/<int:clothes_id>/edit',
         views.clothes_edit,
         name='clothes-edit'),
    path('htmx/clothes/<int:clothes_id>/delete',
         views.clothes_delete,
         name='clothes-delete'),
    # path('outfit/<int:outfit_id>', views.OutfitDetail.as_view(), name='detail'),
    # path('outfit/<int:outfit_id>/delete', views.OutfitDelete.as_view(), name='delete'),
]
