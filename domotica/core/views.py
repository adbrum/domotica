from django.shortcuts import render
import time
import paho.mqtt.client as paho
from gpiozero import LED

led1 = LED(17)
led2 = LED(18)
led3 = LED(22)

# define callback


def on_message(client, userdata, message):
    time.sleep(1)
    print("received message =", str(message.payload.decode("utf-8")))


def clientConnect(request):
    state = request.GET.get('state')
    place = request.GET.get('place')
    print('STATE: ', state)
    print('PLACE: ', place)
    broker = "192.168.1.12"
    # create client object client1.on_publish = on_publish #assign function to callback client1.connect(broker,port) #establish connection client1.publish("house/bulb1","on")
    client = paho.Client("client-001")
    # Bind function to callback
    client.on_message = on_message
    #####
    print("connecting to broker ", broker)
    client.connect(broker)  # connect
    client.loop_start()  # start loop to process received messages
    print("subscribing ")
    client.subscribe(place)  # subscribe
    if place == 'sala':
        led1.toggle()
    elif place == 'quarto':
        led2.toggle()
    elif place == 'cozinha':
        led3.toggle()
    time.sleep(1)
    print("publishing ")
    client.publish(place, state)  # publish
    time.sleep(1)
    client.disconnect()  # disconnect
    client.loop_stop()  # stop loop
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
