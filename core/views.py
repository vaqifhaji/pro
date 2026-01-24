from urllib import request
from django.shortcuts import render

# Create your views here.
def homepage (request):
    return render(request, 'index.html') 
def about (request):
    return render(request, 'about.html')
def shop (request):
    return render(request, 'shop.html')
def faq (request):
    return render(request, 'faq.html')
def contact (request):  
    return render(request, 'contact.html')
def cart (request):
    return render(request, 'cart.html')
def checkout (request):
    return render(request, 'checkout.html')
def blog (request):
    return render(request, 'blog.html') 
def shop_left_sidebar (request):
    return render(request, 'shop-left-sidebar.html')
def wishlist (request):
    return render(request, 'wishlist.html')
def single_product (request):
    return render(request, 'single-product.html')