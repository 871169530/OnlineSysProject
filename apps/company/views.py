from django.views import View
from django.http import HttpResponse



class CompanyIndex(View):
    def get(self, request):
        return HttpResponse('hellp')