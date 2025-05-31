from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_listing, name='create_listing'),
    path('', views.get_listings, name='get_listings'),
]  
