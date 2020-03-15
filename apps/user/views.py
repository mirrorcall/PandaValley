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
    """
    JoinView is a django view for user linking /api/join
    Performing join (sign up) action
    Only accepting POST method
    """
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
            response['msg'] = 'Request failed to get. ' + str(e)

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
            response['msg'] = 'Request failed to get. ' + str(e)

        return JsonResponse(response)
