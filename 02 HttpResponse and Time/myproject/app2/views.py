from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.utils import timezone
import pytz
# Create your views here.


def morning_message(request):
    time = datetime.datetime.now()
    formatted_time = time.strftime("%d-%m-%Y %H:%M:%S")
    return HttpResponse("<h1>Hello, Good Morning! Now the time is: " + formatted_time + "</h1>" )

def noon_message(request):
    time = datetime.datetime.now()
    formatted_time = time.strftime("%d-%m-%Y %H:%M:%S")
    return HttpResponse("<h1>Hello, Good Afternoon! Now the time is: " + formatted_time + "</h1>" )

def evening_message(request):
    time = datetime.datetime.now()
    formatted_time = time.strftime("%d-%m-%Y %H:%M:%S")
    return HttpResponse("<h1>Hello, Good Evening! Now the time is: " + formatted_time + "</h1>" )

def greeting(request):
    current_time = timezone.now()
    hour = current_time.hour

    if 6 <= hour < 12:
        greeting_message = "Good Morning!"
    elif 12 <= hour < 17:
        greeting_message = "Good Noon!"
    elif 17 <= hour < 21:
        greeting_message = "Good Evening!"

    formatted_time = current_time.strftime("%d-%m-%Y %H:%M:%S") 
    return HttpResponse(f"{greeting_message}! Today the date and time is: {formatted_time}")


def message(request):
    current_time_utc = timezone.now()
    ist_tz = pytz.timezone("Asia/Kolkata")
    current_time_ist = current_time_utc.astimezone(ist_tz)

    hour = current_time_ist.hour

    if 6 <= hour < 12:
        greeting_msg = "Hello Student! Good Morning!"
    elif 12 <= hour < 17:
        greeting_msg = "Hello Student! Good Noon!"
    elif 17 <= hour < 21:
        greeting_msg = "Hello Student! Good Evening!"
    else:
        greeting_msg = "Hello Guest!"

    formatted_time = current_time_ist.strftime("%d-%m-%Y %H:%M:%S")
    return HttpResponse(f"{greeting_msg}! Today the date and time in India is: {formatted_time}")

