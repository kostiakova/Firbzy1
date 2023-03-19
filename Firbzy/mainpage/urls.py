from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index),
    path('about_us', views.about),
    path('itemspage', views.item),
    path('item1', views.itemselector1),
    path('item2', views.itemselector2),
    path('item3', views.itemselector3),
    path('item4', views.itemselector4),
    path('contact_us', views.contacts),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)