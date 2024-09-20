from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('Hello, World!')

def index(request):
    return render(request, 'index.html')