from django.shortcuts import render
import time
#from gpiozero import LED

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
        led1.toggle()
    elif place == 'quarto':
        led2.toggle()
    elif place == 'cozinha':
        led3.toggle()

    elif place == 'estore_sala':
        global blind_pos

        if state == 'true' or blind_pos < 100:
            blind_1up.on()
            sleep(2)
            blind_1up.off()
            blind_pos = (blind_pos + 25)


        elif state == 'false' or blind_pos >= 100:
            blind_1dw.on()
            sleep(2)
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
