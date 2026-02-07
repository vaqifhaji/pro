from django.urls import path
from core import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('about/', views.about, name='about'),
    path('shop/', views.shop, name='shop'),
    path('faq/', views.faq, name='faq'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),
    path('checkout/', views.checkout, name='checkout'),
    path('cart/', views.cart, name='cart'),
    path('shop-left-sidebar/', views.shop_left_sidebar, name='shop_left_sidebar'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('single-product/', views.single_product, name='single_product'),
    path('compare/', views.compare, name='compare'),
    path('my-account/', views.my_account, name='my_account'),
    path('login/', views.login_register, name='login'),
    path('mobile-menu/', views.mobile_menu, name='mobile_menu')
]