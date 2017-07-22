from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import View
# def index(requests):
#     if requests.method == 'GET':
#         return HttpResponse('I am called from a get response')
#     elif requests.method == 'POST':
#         return  HttpResponse("I am called from a post response")


class Index(View):
    def get(self, request):
        #return HttpResponse('I am called from a get resquest!!!')
        params = {}
        params["name"] = "liujinmou and yujiang"
#        return render_to_response('base.html')
        return render(request, 'base.html', params)

    def post(self, request):
        return HttpResponse("I am called from a post request!!!")