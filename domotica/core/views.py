from django.shortcuts import render


def index(request):
    return render(request, 'core/index.html')


def lighting(request):
    return render(request, 'core/lighting.html')


def surveillance(request):
    print(request)
    return render(request, 'core/surveillance.html')

# from django.http import HttpResponse


# def index(request):
#   return HttpResponse("Hello, world. You're at the polls index.")
