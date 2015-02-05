from django.shortcuts import render
from rest_framework import serializers
from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.


def addData(request):
	return HttpResponse("Hello Beta")