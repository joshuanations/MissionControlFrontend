from django.shortcuts import render


def home(request):
    return render(request, 'frontend_app/home.html')


def about(request):
    return render(request, 'frontend_app/about.html')
