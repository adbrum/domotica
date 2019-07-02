from django.shortcuts import render
import time
from gpiozero import LED

led1 = LED(20)
led2 = LED(21)
led3 = LED(16)

def on_message(client, userdata, message):
    time.sleep(1)
    print("received message =", str(message.payload.decode("utf-8")))


def clientConnect(request):
    state = request.GET.get('state')
    place = request.GET.get('place')
    print('STATE: ', state)
    print('PLACE: ', place)

    if place == 'sala':
        led1.toggle()
    elif place == 'quarto':
        led2.toggle()
    elif place == 'cozinha':
        led3.toggle()
    time.sleep(1)
    return render(request, 'core/index.html')


def index(request):
    return render(request, 'core/index.html')


def lighting(request):
    print(request)
    return render(request, 'core/lighting.html')


def surveillance(request):
    print(request)
    return render(request, 'core/surveillance.html')


def cam01(request):
    print(request)
    return render(request, 'core/cam_01.html')
