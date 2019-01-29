from django.shortcuts import render


def index(request):
    return render(request, 'core/index.html')


def lighting(request):
    print(request)
    return render(request, 'core/lighting.html')

# from django.http import HttpResponse


# def index(request):
#   return HttpResponse("Hello, world. You're at the polls index.")
