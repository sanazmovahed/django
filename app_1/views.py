from json.encoder import JSONEncoder
from django.http import response
from django.shortcuts import render
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from app_1.models import User, Token, Income, Expense
from datetime import datetime

# Create your views here.
@csrf_exempt
def submit_expense(request):
    """ User submits an expense """ 
    print ("We are in the page of submitting expense!")
    print(request.POST)
    this_token = request.POST['token']
    this_user = User.objects.filter(token__token = this_token).get()
    if 'date' not in request.POST:
        date = datetime.now()
    Expense.objects.create(user = this_user, amount = request.POST['amount'], text = request.POST['text'], date = date)
    return JsonResponse({
        'status' : 'ok'
    }, encoder=JSONEncoder)
    
    
@csrf_exempt
def submit_income(request):
    """ User submits an income """ 
    print ("We are in the page of submitting income!")
    print(request.POST)
    this_token = request.POST['token']
    this_user = User.objects.filter(token__token = this_token).get()
    if 'date' not in request.POST:
        date = datetime.now()
    Income.objects.create(user = this_user, amount = request.POST['amount'], text = request.POST['text'], date = date)
    return JsonResponse({
        'status' : 'ok'
    }, encoder=JSONEncoder)
     