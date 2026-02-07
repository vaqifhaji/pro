import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from product.models import Product


products_data = [
    {
        'name': 'Hand-Made Garlic Mortar', 
        'image': 'garlic-mortar.jpg', 
        'description': 'Beautiful handmade garlic mortar', 
        'price': 38.50, 
        'stock': 15
    },
    {
        'name': 'Handmade Ceramic Pottery', 
        'image': 'ceramic-pottery.jpg',
        'description': 'Unique ceramic pottery handcrafted', 
        'price': 45.50, 
        'stock': 20
    },
    {
        'name': 'Hand Painted Bowls', 
        'image': 'painted-bowls.jpg',
        'description': 'Colorful hand-painted ceramic bowls', 
        'price': 28.50, 
        'stock': 12
    },
    {
        'name': 'Wooden Serving Tray', 
        'image': 'wooden-tray.jpg',
        'description': 'Elegant wooden serving tray', 
        'price': 32.00, 
        'stock': 10
    },
    {
        'name': 'Handwoven Basket', 
        'image': 'handwoven-basket.jpg',
        'description': 'Durable handwoven basket for storage', 
        'price': 22.75, 
        'stock': 25
    }
]

for data in products_data:
    product, created = Product.objects.get_or_create(name=data['name'], defaults=data)
    if created:
        print(f'Created: {product.name}')
    else:
        print(f'Exists: {product.name}')

print('Done!')
