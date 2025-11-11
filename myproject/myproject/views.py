from django.http import HttpResponse

def home(request):
    return HttpResponse("""
        <h1>Available Paths</h1>
        <ul>
            <li><a href='/insta/feed/'>Insta Feed</a></li>
            <li><a href='/insta/addpost/'>Add Post</a></li>
            <li><a href='/insta/profile/'>Profile</a></li>
            <li><a href='/accounts/login/'>Login</a></li>
        </ul>
    """)
