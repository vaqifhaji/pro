from django.shortcuts import render

# Create your views here.
def my_account(request):
    return render(request, 'my-account.html')

def login_register(request):
    return render(request, 'login.html')
