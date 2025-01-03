from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('user/register/', views.user_registration, name='user_registration'),
    path('user/login/', views.user_login, name='user_login'),
    path('staff/register/', views.staff_registration, name='staff_registration'),
    path('staff/login/', views.staff_login, name='staff_login'),
    path('item/register/', views.item_registration, name='item_registration'),
    path('item/all/', views.items_list, name='items_list'),
    path('product/all/', views.products_list, name='products_list'),
]