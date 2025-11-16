from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')

def analytics(request):
    return render(request, 'main/analytics.html')