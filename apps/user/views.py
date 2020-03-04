from django.http import JsonResponse
from django.views.generic.base import View

from .models import UserProfile


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
            user_profile.password = request.POST.get('password')
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
            response['msg'] = str(e)

        return JsonResponse(response)
