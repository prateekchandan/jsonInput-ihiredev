from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from jsonInput.models import payments
from jsonInput.serializers import paymentSerializer

# Create your views here.

@api_view(['POST','GET'])
def addData(request):
    if request.method == 'GET':
        snippets = payments.objects.all()
        serializer = paymentSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        #request.data['sourceTxid'] = request.data['paymentId']
        #request.data['outAsset'] = request.data['asset']
        #request.data['outAmount'] = request.data['amount']
        serializer = paymentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)