from django.urls import path
from .views import *
from core import views
urlpatterns = [
    path('', views.homepage, name='home'),
    path('about/', views.about, name = 'about'),
    path('shop/', views.shop, name = 'shop'),
    path('faq/', views.faq, name = 'faq'),
    path('contact/', views.contact, name = 'contact'),
    path('blog/',  views.blog, name = 'blog'),
    path('checkout/', views.checkout, name = 'checkout'),
    path('cart/', views.cart, name = 'cart'),
    path('shop-left-sidebar.html', views.shop_left_sidebar, name='shop_left_sidebar'),
    path('wishlist.html', views.wishlist, name='wishlist'),
    path('single-product.html', views.single_product, name='single_product'),


]