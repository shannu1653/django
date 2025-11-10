from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.db import connection
import json
from django.views.decorators.csrf import csrf_exempt
from .models import Student  # ✅ Correct import from models
from .models import PostData

# Simple views
def sample(request):
    return HttpResponse('hello world!')

def sample1(request):
    return HttpResponse('welcome to django')

def sampleInfo(request):
    data = {'name': 'shannu', 'age': '23', 'city': 'Vizianagaram'}
    return JsonResponse(data)

def dynamicResponse(request):
    name = request.GET.get("name", "Guest")
    city = request.GET.get('city', 'hyd')
    return HttpResponse(f"hello {name} from {city}")

def add(request):
    a, b = 2, 4
    return HttpResponse(f"addition of two numbers {a} + {b} is {a+b}")

def sub(request):
    a, b = 10, 20
    return HttpResponse(f"The subtraction of two numbers {a} - {b} is {a-b}")

def health(request):
    try:
        with connection.cursor() as c:
            c.execute("SELECT 1")
        return JsonResponse({"status": "ok", "db": "connected"})
    except Exception as e:
        return JsonResponse({"status": "error", "db": str(e)})

# Add student view
@csrf_exempt
def addStudent(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            student = Student.objects.create(
                name=data.get('name'),
                age=data.get('age'),
                email=data.get('email')
            )
            return JsonResponse({"status": "success", 'id': student.id}, status=200)
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=400)
    return JsonResponse({"error": "use POST method"}, status=400)


#postdata
@csrf_exempt
def post(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            postdata = PostData.objects.create(
                post_name=data.get('postname'),
                post_type=data.get('posttype'),
                post_date=data.get('date'),
                post_description=data.get('postdesc')
            )

            return JsonResponse({"status": "success", "id": postdata.id}, status=200)

        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=400)

    return JsonResponse({"error": "use POST method"}, status=400)
