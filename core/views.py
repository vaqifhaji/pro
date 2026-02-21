from django.shortcuts import render
from product.models import Product

# Create your views here.
def homepage(request):
    products = Product.objects.all()[:8]
    return render(request, 'index.html', {'products': products})

def about(request):
    return render(request, 'about.html')

def shop(request):
    products = Product.objects.all()
    return render(request, 'shop.html', {'products': products})

def faq(request):
    return render(request, 'faq.html')

def contact(request):
    return render(request, 'contact.html')



def checkout(request):
    return render(request, 'checkout.html')

def blog(request):
    return render(request, 'blog.html')

def shop_left_sidebar(request):
    products = Product.objects.all()
    # template 'shop-left-sidebar.html' was missing in the project; render the
    # existing 'shop.html' as a fallback so the route works and products display.
    return render(request, 'shop.html', {'products': products})

def wishlist(request):
    return render(request, 'wishlist.html')

def single_product(request):
    return render(request, 'single-product.html')
    
def compare(request):
    return render(request, 'compare.html')

def my_account(request):
    return render(request, 'my-account.html')

def login_register(request):
    return render(request, 'login.html')

def mobile_menu(request):
    return render(request, 'mobile_menu.html') 