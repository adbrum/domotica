from django.shortcuts import render
import time
from gpiozero import LED
from json_response import JsonResponse

light_1 = LED(16)
light_2 = LED(20)
light_3 = LED(21)

blind_1up = LED(17)
blind_1dw = LED(18)

blind_pos = 25
context = {}

state1 = 0
state2 = 0
state3 = 0

def on_message(client, userdata, message):
    time.sleep(1)
    print("received message =", str(message.payload.decode("utf-8")))

def clientConnect(request):
    state = ''
    global blind_pos
    global context
    global state1
    global state2
    global state3

    state = request.GET.get('state')
    place = request.GET.get('place')
    print('STATE: ', state)
    print('PLACE: ', place)

    if place == 'sala':
        light_1.toggle()
        state1 = light_1.value
    elif place == 'quarto':
        light_2.toggle()
        state2 = light_2.value
    elif place == 'cozinha':
        light_3.toggle()
        state3 = light_3.value

    elif place == 'estore_sala':

        if (state == 'true' and blind_pos < 100) and blind_1dw.value == 0:
            blind_1up.on()
            time.sleep(2)
            blind_1up.off()
            #blind_pos = (blind_pos + 25)
            #print('blind_pos < 100', blind_pos)

        elif (state == 'false' and blind_pos > 0) and blind_1up.value == 0:
            blind_1dw.on()
            time.sleep(2)
            blind_1dw.off()
            #blind_pos = (blind_pos - 25)
            #print('blind_pos > 0', blind_pos)

    ''' context = {
        "state1": light_1.value,
        "state2": light_2.value,
        "state3": light_3.value
    } '''

    #print('state1: ', light_2.value)
    #print('BLIND = ', blind_pos)


    time.sleep(1)
    return render(request, 'core/index.html')

def index(request):
    return render(request, 'core/index.html')

def lighting(request):
    print(request)

    context = {
            "state1": state1,
            "state2": state2,
            "state3": state3,
            "blind_pos": blind_pos
            }

    for key, value in context.items():
        print(key, ":", value)

    return render(request, 'core/lighting.html',
                {
            "state1": state1,
            "state2": state2,
            "state3": state3,
            "blind_pos": blind_pos
            })

def blindPosition(request):
    global blind_pos
    state = request.GET.get('state')
    place = request.GET.get('place')
    print('blindPosition: ', state)
    print('blindPosition: ', place)
    if place == 'estore_sala':
        if (state == 'true' and blind_pos < 100) and blind_1dw.value == 0:
                blind_1up.on()
                time.sleep(2)
                blind_1up.off()
                blind_pos = (blind_pos + 25)
                print('blind_pos < 100', blind_pos)

        elif (state == 'false' and blind_pos > 0) and blind_1up.value == 0:
                blind_1dw.on()
                time.sleep(2)
                blind_1dw.off()
                blind_pos = (blind_pos - 25)
                print('blind_pos > 0', blind_pos)

    data = {
        "blind_pos": blind_pos
    }
    return JsonResponse(data)

def surveillance(request):
    print(request)
    return render(request, 'core/surveillance.html')

def cam01(request):
    print(request)
    return render(request, 'core/cam_01.html')
