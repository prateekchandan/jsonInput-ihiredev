from django.forms import widgets
from rest_framework import serializers
from django.shortcuts import render
from django.http import HttpResponse
import json

def index(request):
	ctx = {}
	ctx["error"] = 404
	ctx["message"] = "URL Not Found"
	return HttpResponse(json.dumps(ctx),content_type='application/json',status=404)