
from django.contrib import admin
from django.urls import path, include
from .views import shop_item_list, help_view, contact_view

urlpatterns = [
    
    path('',shop_item_list ),
    path('help', help_view),
    path('contact', contact_view)
]
