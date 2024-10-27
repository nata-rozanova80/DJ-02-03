
from django.shortcuts import render

def home_view(request):
    return render(request, 'myapp/index.html')

def data_view(request):
    return render(request, 'myapp/data.html')

def test_view(request):
    return render(request, 'myapp/test.html')

def new(request):
    return render(request, 'myapp/new.html')

def privacy_policy(request):
    return render(request, 'myapp/privacy policy.html')

def contacts(request):
    return render(request, 'myapp/contacts.html')



