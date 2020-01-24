from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect

from .forms import *
from .models import *

from rest_framework.views import APIView
from rest_framework.decorators import api_view , permission_classes
from rest_framework.response import Response



def Register(request):
    Profile.objects.all().delete()
    if request.method == 'POST':
        rgst_form = RegisterForm(request.POST or None)
        form    = UserCreationForm(request.POST)
        
        error = ''
        context = {

                'rgst_form' : rgst_form,
                'form'      : form,
                }

        if form.is_valid() and rgst_form.is_valid():
            form.save()

            users     = User.objects.all()
            username  = form.cleaned_data['username']
            firstname = rgst_form.cleaned_data.get("firstname")
            lastname  = rgst_form.cleaned_data.get("lastname")
            email     = rgst_form.cleaned_data.get("email")
            for x in users:
                if x.email == email:
                    error = "your email is duplicate"
                    return redirect("users/Register")

            target_user = User.objects.get(username=username)
            
            # token = Token.objects.create(user=target_user)

            target_user.email = email
            target_user.first_name = firstname
            target_user.last_name  = lastname
            target_user.save()
            

            address_obj = UserAddress(address= None, state_choice=None, city_choice=None, post_code =None)
            address_obj.save()

            profile = Profile(user=target_user, address=address_obj, email=email)
            profile.save()


            context = {
                'error'     : error,
                'rgst_form' : rgst_form,
                'form'      : form,
                }
            return redirect('/')
    else:
        
        form = UserCreationForm()
        rgst_form = RegisterForm(request.POST or None)

        context = {
                'rgst_form' : rgst_form,
                'form'      : form,
            }
    return render(request, 'registration/Register.html', context)


#+========================================================================================================
#=============================================== PROFILE =================================================

class ClassProfile(View):

    form_class1 = ProfileForm
    form_class2 = AddressForm
    models = User , Profile
    template_name = 'user/profile.html'

    def get(self, request, *args, **kwargs):
        
        # get user information from User
        User_details    = User.objects.get(username=request.user)
        # get profile name for add details
        Profile_details = Profile.objects.get(user=request.user)
        # Add profile_Form and address_form from Forms.py in tempalate
        profile_form = self.form_class1(request.GET)
        address_form = self.form_class2(request.GET)

        context = {
            "user_details" : User_details,
            "profile_details" : Profile_details,
            'edprf_form'   : profile_form,
            'address_form' : address_form,
        }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):

        # get user information from User
        User_details    = User.objects.get(username=request.user)
        # get profile name for add details
        Profile_details = Profile.objects.get(user=request.user)
        # Add profile Form from Forms.py
        profile_form = self.form_class1(request.POST)
        address_form = self.form_class2(request.POST)

        if profile_form.is_valid():
            # Choice user From User Model
            user_rgst  = User.objects.get(username=request.user)

            # get Profile Details From Template
            national_code = profile_form.cleaned_data['national_code']
            phone_numb    = profile_form.cleaned_data['phone_numb']

            profile = Profile.objects.get(user=request.user)
            profile.national_code = national_code
            profile.phone_numb = phone_numb
            profile.save()

        if address_form.is_valid():
            # get address Details From Template
            post_code = address_form.cleaned_data['post_code']
            state     = address_form.cleaned_data['state']
            city      = address_form.cleaned_data['city']
            address   = address_form.cleaned_data['address']

            statestr = ''.join(state)
            citystr  = ''.join(city)
            print(statestr," %%%%%%%%%%%%%%% ",citystr)

            # Add Details For Address
            # Add address In database
            address_obj = UserAddress(state_choice = statestr, city_choice = citystr, address = address, post_code = post_code)
            address_obj.save()

            #Get User From Profile and add Details in profile 
            profile = Profile.objects.get(user=request.user)
            profile.address = address_obj
            profile.save()

        context = {
            "user_details" : User_details,
            "profile_details" : Profile_details,
            'edprf_form' : profile_form,
            'address_form' : address_form,
            }

        return render(request, self.template_name, context)

#================================================================================================================
