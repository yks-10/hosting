from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from .serializer import CommonSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
import smtplib
# Create your views here.
class CommonView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        c = Common.objects.all()
        s = CommonSerializer(c, many=True)
        return Response(s.data)

    def post(self, request):
        s = CommonSerializer(data=request.data)
        if s.is_valid():
            s.save()
            return Response(s.data, status=status.HTTP_200_OK)
        return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)


class EmailView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("yogeshkrishnan.yks00@gmail.com","YogeshS10.11")
        message = "Message"
        s.sendmail("yogeshkrishnan.yks00@gmail.com", "venkatjai.j@gmail.com", message)
        s.quit()
        data ={
            "Done":"Done"
        }
        return Response(data, status.HTTP_200_OK)