from django.shortcuts import render
from django.http import HttpResponse

import main.models

from django.views.decorators.crsf import csrf_exempt #all calls in django need csrf, this makes it so we dont need it. It's annoying right now 
#and bad practice but that's fine

import unittest


import json


# Create your views here.
@csrf_exempt
def login(request):
	try:
		if request.method = "POST" and request.META.get('CONTENT_TYPE') == "application/json":
			req_load = json.loads(request.body)
			login_count = UserModel.objects.login(username = req_load['user'], pswd = req_load['password']) #this value also might be negative for errs
			res_to_return = {}
			if login_count == SUCCESS:
				res_to_return['login'] = login_count
				res_to_return['errCode'] = login_count
			else:  
				res_to_return['errCode'] = login_count
			return HttpResponse(json.dumps(res_to_return, content_type= "application/json"))
	except:
		return HttpResponse(status=500)

@csrf_exempt
def add(request):
	try:
		if request.method = "POST" and request.META.get('CONTENT_TYPE') == "application/json":
			req_load = json.loads(request.body)
			login_count = UserModel.objects.add(username = req_load['user'], pswd = req_load['password'])
			res_to_return = {}
			if login_count == SUCCESS:
				res_to_return['errCode'] = 1
				res_to_return['count'] = login_count
			else:
				res_to_return['errCode'] = login_count
			return HttpResponse(json.dumps(response), content_type="application/json")
	except:
		return HttpResponse(status = 500)


@csrf_exempt
def TESTAPI_resetFixture(request):
	if request.method = "POST" and request.META.get('CONTENT_TYPE') == "application/json":
		pass
	return HttpResponse("still to be done")



@csrf_exempt
def TESTAPI_test(request):
	if request.method = "POST" and request.META.get('CONTENT_TYPE') == "application/json":	
		pass
	return HttpResponse("still to be done")



