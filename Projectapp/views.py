from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

def temp(request):
    json = {"Message": "Hello WorlD"}
    return JsonResponse(json)