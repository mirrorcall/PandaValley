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

# class LogoutView(View):
#     def get(self,request):
#         #log out
#         #clear session
#         logout(request)
#         #request.session.clear()
#         #request.session.flush()
#         #clear cookies
#         #response = redirect(reverse()) #later need changes
#         # response.delete_cookie('email')
#         # response.delete_cookie('password')
#         return None

from django.core.mail import send_mail
import base64

#from django.core.validators import validate_email

class ForgetPassword(View):
    def post(self,request):
        response = {}
        try:
            email = request.POST.get('email')
            #check if the email is resigerested
            if UserProfile.objects.get(email=email):
            #    response['msg'] = 'Invalid email.'
                #encryption
                code = email.encode("utf-8")   #  decodebytes
                code = base64.encodebytes(code)
                mail_title = 'Forgot password with PandaValley'
                mail_body = 'Click the link to rest your password: http://127.0.0.1:8000/api/emailvalidation?token=%s'%code
                send_state = send_mail(mail_title,mail_body,'PandaValley@163.com',[email])
                response['code'] = 2
                response['msg'] = 'Sent email.'
            else:
                response['code'] = 1
                response['msg'] = 'Invalid email.'

        except Exception as e:
            response['code'] = 0
            response['msg'] = 'Request failed to get %s.'%e
        return JsonResponse(response)

class EmailValidation(View):
    def get(self,request):
        response = {}
        try:
            token = request.GET.get('token')
            email = base64.decodebytes(token).decode("utf-8")
            user = UserProfile.objects.filter(email=email)
            response['msg'] = email
        except Exception as e:
            response['code'] = 0
            response['msg'] = 'Request failed to get %s.'%e
        return JsonResponse(response)

class ResetPassword(View):
    def post(self,request):
        response = {}
        try:
            email = request.POST.get('email')
            new_password = request.POST.get('newpassword')
            user = UserProfile.objects.get(email=email)
            user.password = new_password
            user.save()
            response['msg'] = 'Successful change the password.'
        except Exception as e:
            response['code'] = 0
            response['msg'] = 'Request failed to get %s.'%e
        return JsonResponse(response)
