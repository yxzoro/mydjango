
from django.http import HttpResponse
from django.views.generic import View

# if need to operate db:
# from db.models import Apple 


class X(View):
    def get(self, request):
        print vars(request)
        print request.body
        return HttpResponse('get ok')

    def post(self, request):
        print request.POST
        print request.body
        return HttpResponse('--')

    def delete(self, request):
        print request.body
        return HttpResponse('delete')
