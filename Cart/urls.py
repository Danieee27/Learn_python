from django.urls import path
from . import views


urlpatterns = [
    path('', views.Cart_summary, name = 'Cart_summary'),
    path('add/', views.Cart_add, name = 'Cart_add'),
    path('delete/', views.Cart_summary, name = 'Cart_delete'),
    path('update', views.Cart_summary, name = 'Cart_update'),

]
