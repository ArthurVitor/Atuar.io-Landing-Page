from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='sobre'),
    path('services/', views.services, name='servicos'),
    path('prices/', views.prices, name='precos'),
    path('blog/', views.blog, name='blog'),
    path('detail/', views.detail, name='detail'),
]