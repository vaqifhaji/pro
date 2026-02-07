from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from product.models import Product
import os

class Command(BaseCommand):
    help = 'Add sample products to the database'

    def handle(self, *args, **options):
        products_data = [
            {
                'name': 'Hand-Made Garlic Mortar',
                'description': 'Beautiful handmade garlic mortar made with natural stone and wooden pestle.',
                'price': 38.50,
                'stock': 15,
                'image': 'product-image/1.jpg'
            },
            {
                'name': 'Handmade Ceramic Pottery',
                'description': 'Unique ceramic pottery handcrafted by skilled artisans.',
                'price': 38.50,
                'stock': 20,
                'image': 'product-image/2.jpg'
            },
            {
                'name': 'Hand Painted Bowls',
                'description': 'Colorful hand-painted ceramic bowls perfect for decoration or use.',
                'price': 38.50,
                'stock': 12,
                'image': 'product-image/3.jpg'
            },
            {
                'name': 'Antique Wooden Farm Large',
                'description': 'Authentic antique wooden farm tool restored to perfection.',
                'price': 38.50,
                'stock': 8,
                'image': 'product-image/4.jpg'
            },
            {
                'name': 'Handmade Jute Basket',
                'description': 'Natural jute basket handwoven with excellent craftsmanship.',
                'price': 38.50,
                'stock': 25,
                'image': 'product-image/6.jpg'
            },
            {
                'name': 'Knitting yarn & crochet hook',
                'description': 'Premium quality knitting yarn bundle with professional crochet hooks.',
                'price': 38.50,
                'stock': 30,
                'image': 'product-image/7.jpg'
            },
            {
                'name': 'David Head Portraits',
                'description': 'Beautiful sculptured head portraits inspired by classical art.',
                'price': 38.50,
                'stock': 5,
                'image': 'product-image/8.jpg'
            },
            {
                'name': 'Solid wood cherry paddle',
                'description': 'Authentic solid wood cherry paddle, perfect for cooking or decoration.',
                'price': 38.50,
                'stock': 18,
                'image': 'product-image/9.jpg'
            },
        ]

        for data in products_data:
            product, created = Product.objects.get_or_create(
                name=data['name'],
                defaults={
                    'description': data['description'],
                    'price': data['price'],
                    'stock': data['stock'],
                }
            )
            
            # Try to link to static image
            image_path = os.path.join('C:\\Users\\vaqif\\OneDrive\\Desktop\\pro\\static', data['image'])
            if os.path.exists(image_path):
                with open(image_path, 'rb') as f:
                    product.image.save(os.path.basename(image_path), ContentFile(f.read()), save=True)
            
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created product: {product.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Product already exists: {product.name}'))
