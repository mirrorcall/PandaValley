from django.contrib.auth import authenticate
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import make_password
from django.db.models import Q
from django.http import JsonResponse
from django.views.generic.base import View

from .models import UserProfile


class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user_profile = UserProfile.objects.get(Q(email=username))
            if user_profile.check_password(password):
                return user_profile
        except UserProfile.DoesNotExist:
            return None


# Create your views here.
class JoinView(View):
    def post(self, request):
        response = {}
        try:
            user_profile = UserProfile()
            user_profile.email = request.POST.get('email')
            user_profile.first_name = request.POST.get('first_name')
            user_profile.last_name = request.POST.get('last_name')
            user_profile.telephone = request.POST.get('telephone')
            user_profile.password = make_password(request.POST.get('password'))
            user_profile.is_active = False

            # Handling exception - if email is being registered
            if UserProfile.objects.filter(email=user_profile.email):
                response['code'] = 1
                response['msg'] = 'unsuccessfully creating the user, as the email has been registered'
            else:
                user_profile.save()
                response['code'] = 0
                response['msg'] = 'successfully creating the user'

        except Exception as e:
            response['code'] = 127
            response['msg'] = 'Internal server failure. ' + str(e)

        return JsonResponse(response)


class LoginView(View):
    def post(self, request):
        response = {}
        try:
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(username=email, password=password)
            if not user:
                response['code'] = 1
                response['msg'] = 'failed to authenticate username and password'
            else:
                response['email'] = email
                response['code'] = 0
                response['msg'] = 'successfully login as the user'
        except Exception as e:
            response['code'] = 127
            response['msg'] = 'Internal server failure. ' + str(e)

        return JsonResponse(response)


class PassUserInfoView(View):
    def get(self, request):
        response = {}
        try:
            email = request.GET.get('email')
            user = UserProfile.objects.get(email=email)
            if user.avatar.name:
                response['avatar_url'] = user.avatar.url
            else:
                response['avatar_url'] = ''
            response['c_time'] = str(user.c_time).split('-')[0]
            response['first_name'] = user.first_name
            response['last_name'] = user.last_name
            response['gender'] = user.gender
            response['dob'] = user.dob
            response['phone'] = user.telephone
            response['code'] = 0
        except Exception as e:
            response['code'] = 127
            response['msg'] = 'Internal server failure. ' + str(e)

        return JsonResponse(response)


class UploadAvatarView(View):
    def post(self, request):
        response = {}
        try:
            email = request.POST.get('email')
            user = UserProfile.objects.get(email=email)
            user.avatar = request.FILES.get('avatar')
            print(user.avatar.url)
            user.save()
            response['avatar_url'] = user.avatar.url
            response['code'] = 0
        except Exception as e:
            response['code'] = 127
            response['msg'] = 'Internal server failure. ' + str(e)

        return JsonResponse(response)


class ModifyProfileView(View):
    def post(self, request):
        response = {}
        try:
            email = request.POST.get('email')
            profile_key = request.POST.get('profile_key')
            user = UserProfile.objects.get(email=email)

            if profile_key == 'NAME':
                user.first_name = request.POST.get('profile_value_1')
                user.last_name = request.POST.get('profile_value_2')
            elif profile_key == 'GENDER':
                user.gender = request.POST.get('profile_value_1')
            elif profile_key == 'DOB':
                user.dob = request.POST.get('profile_value_1')

            user.save()
            response['code'] = 0
        except Exception as e:
            response['code'] = 127
            response['msg'] = 'Internal server failure. ' + str(e)

        return JsonResponse(response)
