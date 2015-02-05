from django.db import models

# Create your models here.
class payments(models.Model):
	blockId = models.IntegerField()
	sourceTxid = models.CharField(max_length=500)
	sourceAddress = models.TextField()
	destinationAddress = models.CharField(max_length=1000)
	outAsset = models.TextField(max_length=500)
	outAmount = models.BigIntegerField()
	status = models.CharField(max_length=200)
	lastUpdatedBlockId = models.IntegerField()
	class Meta:
		verbose_name_plural = "payments"