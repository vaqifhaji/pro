from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('my-account/', views.my_account, name='my_account'),
    path('login/', views.login_register, name='login'),
]
