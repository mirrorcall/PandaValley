from django.contrib.auth import authenticate,logout
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
            # if user_profile.password == password:
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
                response['code'] = 101
                response['msg'] = 'unsuccessfully creating the user, as the email has been registered'
            else:
                user_profile.save()
                response['code'] = 100
                response['msg'] = 'successfully creating the user'

        except Exception as e:
            response['code'] = 102
            response['msg'] = 'Request failed to get. ' + str(e)

        return JsonResponse(response)


class LoginView(View):
    def post(self, request):
        response = {}
        try:
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(username=email, password=password)
            print(user)
            if user:
                response['code'] = 200
                response['msg'] = 'successfully login as the user'
            else:
                response['code'] = 201
                response['msg'] = 'failed to authenticate username and password'
        except Exception as e:
            response['code'] = 202
            response['msg'] = 'Request failed to get. ' + str(e)

        return JsonResponse(response)

class LogoutView(View):
    def get(self,request):
        #log out
        response = logout(request)
        #clear cookies
        #response = redirect(reverse()) #later need changes
        response.delete_cookie('email')
        response.delete_cookie('password')
        return response


