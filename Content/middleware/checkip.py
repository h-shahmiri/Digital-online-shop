from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse
from django.shortcuts import redirect
from Content.views import func_prc


class CheckIp(MiddlewareMixin):
    def process_request(self, request):
        ip = request.META.get('REMOTE_ADDR')
        if ip.startswith('126'):
            return HttpResponse(ip)


    def process_view(self, request, func, args, kwargs):
        if func == func_prc:
            print("process_views")

    def process_reponse(self, request, response):
        print(response)