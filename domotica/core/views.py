from django.shortcuts import render


def index(request):
    return render(request, 'core/index.html')

# from django.http import HttpResponse


# def index(request):
#   return HttpResponse("Hello, world. You're at the polls index.")
