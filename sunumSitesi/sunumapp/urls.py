from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='sunumapp-home'),
    path('sayfa1/', views.sayfa1, name='sunumapp-sayfa1'),
    path('sayfa2/', views.sayfa2, name='sunumapp-sayfa2'),
    path('sayfa3/', views.sayfa3, name='sunumapp-sayfa3'),
]