from django.forms import widgets
from rest_framework import serializers
from jsonInput.models import payments
from hashlib import sha256
from future.types import *
 
digits58 = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
 
def decode_base58(bc, length):
    n = 0
    for char in bc:
        n = n * 58 + digits58.index(char)
    print type(n)
    bcbytes = n.to_bytes(length, 'big')
    return bcbytes[-4:] == sha256(sha256(bcbytes[:-4]).digest()).digest()[:4]

def bitCoinUrl(value):
    #try:
    check = decode_base58(value, 25)
    #except Exception, e:
    #    raise serializers.ValidationError('Invalid BItcoin URL.')
    
    if check == False:
        raise serializers.ValidationError('Invalid BItcoin URL.')
    
class paymentSerializer(serializers.Serializer):
    
    blockId = serializers.IntegerField(default=0 ,read_only=True  )
    sourceTxid = serializers.CharField()
    sourceAddress = serializers.CharField()
    destinationAddress = serializers.CharField(max_length=1000)
    outAsset = serializers.CharField(validators=[bitCoinUrl])
    outAmount = serializers.IntegerField()
    status = serializers.CharField(default='authorized' ,read_only=True)
    lastUpdatedBlockId = serializers.IntegerField(default=0,read_only=True)

    def create(self, validated_data):
        return payments.objects.create(**validated_data)

