from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.db import connection
import json
from django.views.decorators.csrf import csrf_exempt
from .models import Student  # ✅ Correct import from models
from .models import PostData,Users
from basic.models import Movie
from django.contrib.auth.hashers import make_password,check_password
import jwt
from django.conf import settings

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
    print(a+b)
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

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Student

@csrf_exempt
def addStudent(request):
    # 1. CREATE (POST)
    if request.method == 'POST':
        data = json.loads(request.body)
        student = Student.objects.create(
            name=data.get('name'),
            age=data.get('age'),
            email=data.get('email'),
            
        )
        return JsonResponse({"status": "success", "id": student.id}, status=200)

    # 2. READ (GET)
    elif request.method == 'GET':

        # FEATURE 1: Order by name
        if request.GET.get("orderby") == "name":
            results = list(Student.objects.order_by('name').values())
            return JsonResponse({"status": "ok", "data": results}, status=200)

        # FEATURE 2: Get distinct ages
        if request.GET.get("distinct") == "age":
            results = list(Student.objects.values('age').distinct())
            return JsonResponse({"status": "ok", "data": results}, status=200)

        # FEATURE 3: Count total students
        if request.GET.get("count") == "all":
            results = Student.objects.count()
            return JsonResponse({"status": "ok", "total_students": results}, status=200)

        # 2.1 GET ALL (no id, no age)
        if not request.GET.get("id") and not request.GET.get("age"):
            result = list(Student.objects.values())
            for i in result:
                print(i)
            return JsonResponse({"status": "ok", "data": result}, status=200)

        # 2.2 GET by ID
        if request.GET.get("id"):
            ref_id = request.GET.get("id")
            results = list(Student.objects.filter(id=ref_id).values())
            if results:
                return JsonResponse({"status": "ok", "data": results}, status=200)
            else:
                return JsonResponse({"status": "error", "message": "Student not found"}, status=404)

        # 2.3 FILTER by Age
        if request.GET.get("age"):
            ref_age = request.GET.get("age")

            filter_type = request.GET.get("type", "gte")   # default = >=

            if filter_type == "gte": 
                results = list(Student.objects.filter(age__gte=ref_age).values())
            else:
                results = list(Student.objects.filter(age__lte=ref_age).values())

            return JsonResponse({"status": "ok", "data": results}, status=200)

    # 3. UPDATE (PUT)
    elif request.method == "PUT":
        data = json.loads(request.body)
        ref_id = data.get("id")

        try:
            student = Student.objects.get(id=ref_id)
        except Student.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Student not found"}, status=404)

        student.name = data.get("name", student.name)
        student.age = data.get("age", student.age)
        student.email = data.get("email", student.email)
        student.save()
        

        updated_data = list(Student.objects.filter(id=ref_id).values())
        return JsonResponse({"status": "success", "updated_data": updated_data}, status=200)

    # 4. DELETE (DELETE)
    elif request.method == "DELETE":
        data = json.loads(request.body)
        ref_id = data.get("id")

        try:
            student = Student.objects.get(id=ref_id)
        except Student.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Student not found"}, status=404)

        deleted_data = list(Student.objects.filter(id=ref_id).values())
        student.delete()

        return JsonResponse({
            "status": "success",
            "message": "Student deleted successfully",
            "deleted_data": deleted_data
        }, status=200)

    # Invalid method
    return JsonResponse({"error": "Method not allowed"}, status=405)



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


@csrf_exempt
def Signup(request):
    if request.method=="POST":
        data=json.loads(request.body)
        print(data)
        user=Users.objects.create(
            username=data.get('username'),
            email=data.get("email"),
            password=make_password(data.get("password"))
        )
        return JsonResponse({"status":"success"},status=200)

from datetime import datetime




#example for jwt token creating jwt token
@csrf_exempt
def login(request):
    if request.method == 'POST':
        data=request.POST
        print(data)

        username = data.get("username")
        print(username)

        password = data.get("password")
        print(password)

        if not username or not password:
            return JsonResponse({
                "status": "failure",
                "message": "username and password required"
            }, status=400)

        try:
            user = Users.objects.get(username=username)
            if check_password(password, user.password):
                print(user.password)
               # token="a json web token"
                #creating jwt token
                payload={"username":username,"email":user.email,"id":user.id}
                token=jwt.encode(payload,settings.SECRET_KEY,algorithm="HS256")
                # FIXED BLOCK ↓↓↓
                # user_data = {
                #     field.name: getattr(user, field.name)
                #     for field in user._meta.fields
                #     if field.name != "password"
                # }

                return JsonResponse({"status": 'successfully logged in',"token":token}, status=200)
            else:
                return JsonResponse({
                    "status": 'failure',
                    "message": 'invalid password'
                }, status=400)

        except Users.DoesNotExist:
            return JsonResponse({
                "status": 'failure',
                "message": 'user not found'
            }, status=400)

    return JsonResponse({"error": "POST method required"}, status=405)






#⚡curd on movie review scenario formdata.
@csrf_exempt
def Movies(request):

    #create
    if request.method == "POST":
        try:
            # data = json.loads(request.body) #whenver
            data=request.POST
            star = data.get("Rating", 0)
            # Convert rating to stars (⭐⭐⭐)
            star_int = int(star)
            rating_save = "⭐" * star_int

            movie = Movie.objects.create(
                Movie_name=data.get("Movie_name"),
                Date=data.get("Date"),
                Budget=data.get("Budget"),
                Rating=rating_save,
            )
            return JsonResponse({"status": "success","Movie name": movie.Movie_name,"Rating": movie.Rating},status=201
            )

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    # elif request.method == "GET":
    #     result = list(Movie.objects.values())
    #     for i in result:
    #         print(i)
    #     return JsonResponse({"status": "ok", "data": result}, status=200)
    
    elif request.method == "GET":
        # get rating value from Postman params
        ref_rating = request.GET.get("Rating")
        ref_rating = float(ref_rating)
        result=[]
        movies = Movie.objects.all().values()
        for m in movies:
            stars = m["Rating"] 
            rating_number = stars.count("⭐")  
            print(rating_number)
            if rating_number>=ref_rating:
                result.append(m) 
        ref_budget=request.GET.get("Budget")
        ref_budget=int(ref_budget[0:-2])
        result=[]
        movies=Movie.objects.all().values()
        for b in movies:
            budget=b["Budget"]
            budget=int(budget[0:-2])
            if budget>=ref_budget:
                result.append(b)
        return JsonResponse({"status": "ok", "data": result}, status=200)
    elif request.method == "DELETE":
        try:
            data = json.loads(request.body)
            ref_id = data.get("id")



            # Get the movie object
            movie = Movie.objects.get(id=ref_id)

            # Take backup before delete
            deleted_movie = {
                "id": movie.id,
                "Movie_name": movie.Movie_name,
                "Date": movie.Date,
                "Budget": movie.Budget,
                "Rating": movie.Rating
            }

            movie.delete()

            return JsonResponse(
                {"status": "deleted successfully", "deleted_movie": deleted_movie},
                status=200
            )

        except Movie.DoesNotExist:
            return JsonResponse({"error": "Movie not found"}, status=404)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)/859

    return JsonResponse({"error": "Method not allowed"}, status=405)
 



 