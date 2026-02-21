from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product-image/')
    image2 = models.ImageField(upload_to='product-image/', blank=True, null=True)
    image3 = models.ImageField(upload_to='product-image/', blank=True, null=True)
    image4 = models.ImageField(upload_to='product-image/', blank=True, null=True)
    stock = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-created_at']
