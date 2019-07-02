from django.shortcuts import render
import time
from gpiozero import LED

light_1 = LED(16)
light_2 = LED(20)
light_3 = LED(21)

blind_1up = LED(17)
blind_1dw = LED(18)

blind_pos = 0

def on_message(client, userdata, message):
    time.sleep(1)
    print("received message =", str(message.payload.decode("utf-8")))

def clientConnect(request):
    state = request.GET.get('state')
    place = request.GET.get('place')
    print('STATE: ', state)
    print('PLACE: ', place)

    if place == 'sala':
        light_1.toggle()
    elif place == 'quarto':
        light_2.toggle()
    elif place == 'cozinha':
        light_3.toggle()

    elif place == 'estore_sala':
        global blind_pos

        if (state == 'true' and blind_pos < 100)  and blind_1dw.value == 0:
            blind_1up.on()
            time.sleep(2)
            blind_1up.off()
            blind_pos = (blind_pos + 25)


        elif (state == 'false' and blind_pos > 0) and blind_1up.value == 0:
            blind_1dw.on()
            time.sleep(2)
            blind_1dw.off()
            blind_pos = (blind_pos - 25)

        print('BLIND = ', blind_pos)

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
