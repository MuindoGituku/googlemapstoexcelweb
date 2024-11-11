from django.urls import path
from . import views

urlpatterns = [
    path('', views.place_search_view, name='place_search'),
]
