from django.urls import path
from .views import homepage , about
urlpatterns = [
    path('', homepage, name = 'home'),
    path('about.html', about, name = 'about')
]