from django.shortcuts import render

# Create your views here.
def wishlist(request):
    return render(request, 'wishlist.html')

def single_product(request):
    return render(request, 'single-product.html')
    
def compare(request):
    return render(request, 'compare.html')
