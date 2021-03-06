from django.forms import widgets
from rest_framework import serializers
from jsonInput.models import payments
from hashlib import sha256
import re
 
digits58 = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
 
def decode_base58(bc, length):
    n = 0
    for char in bc:
        n = n * 58 + digits58.index(char)
    print type(n)
    bcbytes = ('%%0%dx' % (length << 1) % n).decode('hex')[-length:]
    return bcbytes[-4:] == sha256(sha256(bcbytes[:-4]).digest()).digest()[:4]

def bitCoinUrl(value):
    try:
        check = decode_base58(value, 25)
    except Exception, e:
        raise serializers.ValidationError('Invalid BItcoin URL.')
    
    if check == False:
        raise serializers.ValidationError('Invalid BItcoin URL.')
    
def alphaNumeric(value):
    regex = re.compile("^([A][0-9]+)$|^([B][A-Za-z]+)$")
    if not (regex.match(value)): 
        raise serializers.ValidationError('Asset not in Proper Form.')

class paymentSerializer(serializers.Serializer):
    
    amount = serializers.IntegerField(read_only=True)
    blockId = serializers.IntegerField(default=0 ,read_only=True  )
    paymentId = serializers.CharField(source='sourceTxid')
    sourceAddress = serializers.CharField()
    destinationAddress = serializers.CharField(max_length=1000,validators=[bitCoinUrl])
    asset = serializers.CharField(source='outAsset',validators = [alphaNumeric])
    amount = serializers.DecimalField(max_digits=16, decimal_places=8, source='outAmount')
    status = serializers.CharField(default='authorized' ,read_only=True)
    lastUpdatedBlockId = serializers.IntegerField(default=0,read_only=True)

    def create(self, validated_data):
        return payments.objects.create(**validated_data)

