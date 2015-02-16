from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from jsonInput.models import payments
from jsonInput.serializers import paymentSerializer
from rest_framework import *
from rest_framework import permissions
from models import *
import hashlib
import hmac
import base64
from django.db.models import Q
import json

# Create your views here.
@api_view(['POST','GET'])
def addData(request):

    permission = CheckPermission()
    
    if permission.has_permission(request,None) == True:
        pass
    else:
        raise PermissionDenied("Permission Denied")

    if request.method == 'GET':
        snippets = payments.objects.all()
        serializer = paymentSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = paymentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def MyHMAC(key,data):
    digest = hmac.new(str(key), msg=str(data), digestmod=hashlib.sha512).digest()
    signature = digest.encode("hex")
    return signature
    

class CheckPermission(permissions.BasePermission):
    """
    CheckPermission
    """
    def has_permission(self, request, view):
       
        try:
            sign = request.META['HTTP_AUTHORIZATION']
            date = 1#request.META['HTTP_DATE']
            uname = request.META['HTTP_USERID']
            token = request.META['HTTP_ACCESSTOKEN']

        except Exception as e:
            return False
        
        try:
            User =  AccessKeys.objects.get(userId = uname, AccessToken = token)
        except Exception as e:
            User = None

        if User is None:
            return False

        secretKey = User.SecretKey
       

        if request.method == 'GET':
            data = token
        else:
            data = request.body


        newSign = MyHMAC(secretKey,data)

        print data
        print newSign
        print sign
        if newSign != sign:
            return False
        
        return True





        
