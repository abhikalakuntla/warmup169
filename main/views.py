from django.shortcuts import render
from django.http import HttpResponse

import main.models

from django.views.decorators.csrf import csrf_exempt #all calls in django need csrf, this makes it so we dont need it. It's annoying right now 
#and bad practice but that's fine
from main.tests import allTests
import unittest


import json

#GLOBALS:
SUCCESS = 1
ERR_BAD_CREDENTIALS = -1
ERR_USER_EXISTS = -2
ERR_BAD_USERNAME = -3
ERR_BAD_PASSWORD = -4
MAX_USERNAME_LEN = 128
MAX_PASSWORD_LEN = 128


@csrf_exempt
def show(request):
	return HttpResponse("frontend to come")

# Create your views here.
@csrf_exempt
def login(request):
	try:
		if request.method == "POST" and request.META.get('CONTENT_TYPE') == "application/json":
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
		if request.method == "POST" and request.META.get('CONTENT_TYPE') == "application/json":
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
	try:
		if request.method == "POST" and request.META.get('CONTENT_TYPE') == "application/json":
			res_to_return = {}
			res_to_return['errCode'] = UserModel.objects.TESTAPI_resetFixture()
			return HttpResponse(json.dumps(response), content_type= "application/json")
	except:
		return HttpResponse(status=500)



@csrf_exempt
def test(request):
	if request.method == "POST" and request.META.get('CONTENT_TYPE') == "application/json":	
		result = StringIO()
		tests = (allTests,)
		res_to_return = {}
		res_to_return['nrFailed']= 0
		res_to_return['totalTests'] = 0
		for t in tests:
			test = unittest.TestLoader().loadTestsFromTestCase(t)
			testresult = unittest.TextTestRunner(stream = result, verbosity=5).run(test)
			res_to_return['nrFailed'] += len(testresult.failures)
			res_to_return['totalTests'] += testresult.testsRun
		res_to_return['output'] = result.getValue()
		return HttpResponse(json.dumps(response), content_type="application/json", status = 200)
	return HttpResponse(status=200)



