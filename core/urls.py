from django.urls import path
from core import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('about/', views.about, name='about'),
    path('faq/', views.faq, name='faq'),
    path('compare/', views.compare, name='compare'),
    path('mobile-menu/', views.mobile_menu, name='mobile_menu')
    
]