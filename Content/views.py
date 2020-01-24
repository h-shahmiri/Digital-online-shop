from django.shortcuts import render , redirect
from .models import Category, Item
from django.views.generic import ListView , TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from .forms import AdditemForm  
from django.views import View

from Content.serializers import ItemSerializer , ItemListSerializer
from rest_framework import serializers , generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.pagination import PageNumberPagination
# Create your views here.

class ListUser(APIView):
    def get(self, request, format=None):
        usernames = [user.name for user in Item.objects.all()]
        return Response(usernames)


class ListApiUser(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class Pagination(PageNumberPagination):
    page_size = 5


class ItemViewset(ReadOnlyModelViewSet):
    queryset = Item.objects.all()
    pagination_class = Pagination
    serializ = {
        'list' : ItemListSerializer,
        'retrieve' : ItemSerializer,
    }

    def get_serializer_class(self):
        return self.serializ.get(self.action)



#======================================== Index  ============================================================
        
class MobileCat(TemplateView):

    models = Category
    template_name = 'mobilecat.html'

    # def get(self, request, *args, **kwargs):
        
    #     User_details    = User.objects.get(username=request.user)
    #     Profile_details = Profile.objects.get(user=request.user)

    #     context = {
    #         "user_details" : User_details,
    #         "profile_details" : Profile_details,
    #         'edprf_form'   : profile_form,
    #         'address_form' : address_form,
    #     }

    #     return render(request, self.template_name, context)


class LaptopCat(TemplateView):
    models = Category
    template_name = 'laptopcat.html'



class HomeCat(TemplateView):

    models = Category
    template_name = 'homecat.html'