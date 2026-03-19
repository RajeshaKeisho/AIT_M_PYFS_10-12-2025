from django.shortcuts import render
from rest_framework.decorators import api_view, throttle_classes
from rest_framework.response import Response
from .models import Message
from .serializers import MessageSerializer
from .throttles import CustomUserThrottle
# Create your views here.


@api_view(["GET", "POST"])
def message_list(request):
    if request.method == "GET":
        message = Message.objects.all()
        serializer = MessageSerializer(message, many=True)
        return Response(serializer.data)
    
    if request.method == "POST":
        serializer = MessageSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
@api_view(["GET"])
@throttle_classes([CustomUserThrottle])
def limited_view(request):
    return Response({'message':"Limited API"})

from rest_framework.throttling import ScopedRateThrottle
from rest_framework.views import APIView
class ExampleView(APIView):
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'example'

    def get(self, request):
        return Response({"message": "This is a scoped rate-limited API"})