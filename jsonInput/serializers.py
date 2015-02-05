from django.forms import widgets
from rest_framework import serializers
from jsonInput.models import payments

class paymentSerializer(serializers.Serializer):
    
    blockId = serializers.IntegerField(default=0 ,read_only=True  )
    sourceTxid = serializers.CharField()
    sourceAddress = serializers.CharField()
    destinationAddress = serializers.CharField(max_length=1000)
    outAsset = serializers.CharField()
    outAmount = serializers.IntegerField()
    status = serializers.CharField(default='authorized' ,read_only=True)
    lastUpdatedBlockId = serializers.IntegerField(default=0,read_only=True)

    def create(self, validated_data):
        return payments.objects.create(**validated_data)

    class Meta:
        validators = [
           
        ]
