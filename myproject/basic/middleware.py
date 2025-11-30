
from django.http import JsonResponse
import re,json
from basic.models import Users ##for emialMiddleware

class basicMiddleware:
    def __init__(self,get_response): #whenever we start the sever,it will create automatically a middleware object from th erefernce of class
        self.get_response=get_response

    def __call__(self,request): #whenver we make httmp/https request this execute/helps to get th erespons as per the request from the view
        # print(request,"hello")
        if(request.path=="/addstudent/"):
            print(request.method,"method")
            print(request.path,"path")

        elif(request.path=="/post/"):
            print(request.method,"method")
            print(request.path,"path")

        elif(request.path=="/add/"):
            print(request.method,"method")
            print(request.path,"path")

        elif(request.path=="/sam/"):
            print(request.method,"method")
            print(request.path,"path")


        response=self.get_response(request)
        return response
    





class SSCMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self, request):
        if(request.path in ["job1/","/job2/"]):
            ssc_result=request.GET.get("ssc",False)
            if(not ssc_result):
                return JsonResponse(("error"))
            
class UsernameMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self, request):
        if(request.path == "/signup/"):
            data=json.loads(request.body)
            username=data.get("username","")
            #checks username is empty or not
            if not username:
                return JsonResponse({"error":"username should contains 3 to 20 characters"},status=400)
            
             #check uniqueness in database
            if Users.objects.filter(username=username).exists():
                return JsonResponse({"error":"username already exists"},status=400)
            
            #checks length
            if(len(username)<3 or len(username)>20):
                return JsonResponse({"error":"username should contains 3 to 20 characters"},status=400)
            
            #checks startinf and ending
            if username[0] in "._" or username[-1] in "._":
                return JsonResponse({"error":"username should not starts or ends with . or _"},status=400)
            
            #checks allowd characters
            if not re.match(r"^[a-zA-Z0-9._]+$",username):
                return JsonResponse({"error":"username shoulf contains letters,numbers,dot,underscore"},status=400)
            
            #checks .. and __
            if ".." in username or "__"in username:
                return JsonResponse({"erro: cannot have .. or __"},status=400)
        return self.get_response(request)
    
class EmailMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self, request):
        if(request.path == "/signup/"):
            data=json.loads(request.body)
            email=data.get("email","")
            #checks email is empty or not
            if not email:
                return JsonResponse({"error":"username should contains 3 to 20 characters"},status=400)
            
            
            # Basic email pattern
            basic_pattern = r"^[^@]+@[^@]+\.[^@]+$"
            # Strong pattern (better validation)
            strong_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
            if not re.match(strong_pattern,email):
                return JsonResponse({"error":"invalid email format.Use a valid email like exaple@gmail.com"},status=400)
            
            #check uniqueness in database
            if Users.objects.filter(email=email).exists():
                return JsonResponse({"error":"Email already exists"},status=400)
        return self.get_response(request)
    
class PasswordMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self, request):
        if(request.path == "/signup/"):
            data=json.loads(request.body)
            password=data.get("password","")

            #1.Empty check
            if not password:
                return JsonResponse({"error": "password is required"},status=400)
            
            medium_pattern = r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d@$!#%*?&_]{8,}$"

            if not re.match(medium_pattern,password):
                return JsonResponse({"error":"Password must contain at least 8 characters including uppercase,lowercase,number, and special character"},status=400)
        return self.get_response(request)
    

from django.http import JsonResponse


#multiple middlewares,middleware chaining
class MovieReviesMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        # Only validate when API endpoint is /movies/ AND method is POST
        if request.path == "/movies/" and request.method == "POST":

            incoming_data = request.POST

            movie_name = incoming_data.get("Movie_name")
            date = incoming_data.get("Date")
            rating = incoming_data.get("Rating")

            # VALIDATIONS
            if not movie_name:
                return JsonResponse({"error": "Movie_name is required"}, status=400)

            if not date:
                return JsonResponse({"error": "Date is required"}, status=400)

            if not rating:
                return JsonResponse({"error": "Rating is required"}, status=400)

            # Check numeric rating
            try:
                rating = float(rating)
            except:
                return JsonResponse({"error": "Rating must be a number"}, status=400)

            if rating < 0 or rating > 5:
                return JsonResponse(
                    {"error": "Rating should be between 0 and 5"},
                    status=400
                )

        return self.get_response(request)

        