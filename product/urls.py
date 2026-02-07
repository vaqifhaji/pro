from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('wishlist/', views.wishlist, name='wishlist'),
    path('single-product/', views.single_product, name='single_product'),
    path('compare/', views.compare, name='compare'),
]
