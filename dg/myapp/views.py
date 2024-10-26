
from django.shortcuts import render

def home_view(request):
    return render(request, 'myapp/index.html')

def data_view(request):
    return return render(request, 'myapp/data.html')

def test_view(request):
    return return render(request, 'myapp/test.html')

def new(request):
    return render(request, 'myapp/new.html')



