from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import View
from user_profile.models import User

# def index(requests):
#     if requests.method == 'GET':
#         return HttpResponse('I am called from a get response')
#     elif requests.method == 'POST':
#         return  HttpResponse("I am called from a post response")

class Profile(View):
    """User Profile page reachable form /user/<username> URL"""
    def get(self, request, username):
        print(username)
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return HttpResponse("invalid user")
        else:
            print(user.email)

        #        params = dict()()()
#        User.objects.get
#        User.objects.value_list()username
#        user = User.__getattribute__(self);
        return HttpResponse(user.email)

    def post(self, request):
        return HttpResponse("post profile")

class Index(View):
    def get(self, request):
        #return HttpResponse('I am called from a get resquest!!!')
        params = {}
        params["name"] = "liujinmou and yujiang"
#        return render_to_response('base.html')
        return render(request, 'base.html', params)

    def post(self, request):
        return HttpResponse("I am called from a post request!!!")