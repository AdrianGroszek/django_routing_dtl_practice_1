from django.urls import path
from . import views

urlpatterns = [
    path('', views.starting_page, name='starting-page'),
    path('champions', views.champions_page, name='champions-page'),
    path('champions/<str:champion>',
         views.single_champion_page, name='single-champion')
]
