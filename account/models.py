from django.db import models
from django.contrib.auth.models import AbstractUser
# Use JSONField for storing lists on SQLite; avoid postgres-specific ArrayField

class User(AbstractUser):
    phone = models.CharField('phone', max_length=50, null=True, blank=True)
    email = models.EmailField("email address", unique=True)
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    ips = models.JSONField(null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = 'name',

    def get_profile_image(self):
        if self.profile_image:
            return self.profile_image.url
        else:
            return '/static/images/profile.jpg'
        

class BlockedIpAddress(models.Model):
    ip_address = models.GenericIPAddressField()
    reason = models.CharField('Reason', max_length=255, null=True, blank=True)
    blocked_at = models.DateTimeField('Blocked at', auto_now_add=True)

    def __str__(self):
        return f"{self.ip_address}"