from django.urls import path

from . import views


app_name = 'blog'

urlpatterns = [
    # path('', views.HomePage.as_view(), name='homepage'),
    path('', views.home_page, name='homepage'),
    # path('look/<int:post_id>', )
]
