from django.core.mail import send_mail
import base64
#from django.core.validators import validate_email
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


class ForgetPassword(View):
    def post(self, request):
        response = {}
        try:
            email = request.POST.get('email')
            # check if the email is registered
            print(email)
            if UserProfile.objects.get(email=email):
                # encryption
                code = email.encode("utf-8")   # decode bytes
                code = base64.encodebytes(code)
                mail_title = 'Forgot password with PandaValley'
                mail_body = \
                    'Click the link to rest your password: http://127.0.0.1:8000/api/emailvalidation?token=%s' % \
                    code.decode()
                send_state = send_mail(mail_title, mail_body, 'pdvalley.official@gmail.com', [email])
                print(send_state)
                response['code'] = 0
                response['msg'] = 'Sent email.'
            else:
                response['code'] = 1
                response['msg'] = 'Invalid email.'

        except Exception as e:
            response['code'] = 127
            response['msg'] = 'Internal failure' + str(e)
        return JsonResponse(response)


class EmailValidation(View):
    def get(self, request):
        print(request)
        response = {}
        try:
            token = request.GET.get('token')
            email = base64.decodebytes(token.encode()).decode("utf-8")
            user = UserProfile.objects.filter(email=email)
            if user:
                response['email'] = email
                response['code'] = 0
            else:
                response['msg'] = 'Email does not exist.'
                response['code'] = 1
        except Exception as e:
            response['code'] = 127
            response['msg'] = 'Internal server failure ' + str(e)
        return JsonResponse(response)


class ResetPassword(View):
    def post(self, request):
        response = {}
        try:
            email = request.POST.get('email')
            new_password = request.POST.get('new_password')
            user = UserProfile.objects.get(email=email)
            user.password = new_password
            user.save()
            response['msg'] = 'Successful change the password.'
            response['code'] = 0
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
                response['avatar_url'] = 'https://pandavalley-media.s3-ap-southeast-2.amazonaws.com/media/avatar/default_avatar.png'
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
