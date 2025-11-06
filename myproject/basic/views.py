from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

# Create your views here.

def sample(request):
    return HttpResponse('hello world!')


def sample1(request):
    return HttpResponse('welcome to django')

def sampleInfo(request):
    data={'name':'shannu','age':'23','city':'Vizianagaram'}
    #data={'result':[4,2,3,4]}
    return JsonResponse(data)


def dynamicResponse(request):

    name=request.GET.get("name",input("enter your name : "))
    city=request.GET.get('city','hyd')
    return HttpResponse(f"hello {name} from {city}")

def add(request):
    a=2
    b=4
    return HttpResponse(f"additon of two numbers {a} + {b} is {a+b} ")

def sub(request):
    a=10
    b=20
    return HttpResponse(f"The subtraction of two numbers {a} - {b} is {a-b}")
