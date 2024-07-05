from django.shortcuts import render

# Create your views here

def blog(request):
    return render(request, 'base.html')

def detail(request):
    return render(request,'blog/detail.html')