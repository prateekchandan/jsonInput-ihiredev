from django.db import models
import os
import time
import uuid

# Create your models here.
class payments(models.Model):
    blockId = models.IntegerField()
    sourceTxid = models.CharField(max_length=500)
    sourceAddress = models.TextField()
    destinationAddress = models.CharField(max_length=1000)
    outAsset = models.TextField(max_length=500)
    outAmount = models.DecimalField()
    status = models.CharField(max_length=200)
    lastUpdatedBlockId = models.IntegerField()
    class Meta:
        verbose_name_plural = "payments"

def SecretKeyGenerate():
    key = os.urandom(32)
    key = key + str(time.time())
    key = key.encode('base64').strip()
    return key

def AccessTokenGenerate():
    u = uuid.uuid4()
    u = u.bytes + str(time.time())
    u = u.encode('base_64').strip()
    return u

class AccessKeys(models.Model):
    userId = models.CharField(max_length=500)
    AccessToken = models.CharField(max_length=1000 , default = AccessTokenGenerate)
    SecretKey = models.CharField(max_length=1000 , default = SecretKeyGenerate)
    class Meta:
        verbose_name_plural = "AccessKeys"
    