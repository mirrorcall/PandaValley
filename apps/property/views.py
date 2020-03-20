
from django.db.models import Q
from django.http import JsonResponse
from django.views.generic.base import View


from .models import Property,Images

class AddProperty(View):
    def post(self,request):
        response ={}
        try:
            new_property = Property()
            new_property.host = request.POST.get('email')
            new_property.title = request.POST.get('title')
            new_property.host_name = request.POST.get('name')
            new_property.suburb = request.POST.get('suburb')
            new_property.address = request.POST.get('address')
            new_property.latitude = request.POST.get('latitude')
            new_property.longitude = request.POST.get('longitude')
            new_property.property_type = request.POST.get('property_type')
            new_property.description = request.POST.get('description')
            new_property.guests = request.POST.get('guests')
            new_property.bedrooms = request.POST.get('bedrooms')
            new_property.bathrooms = request.POST.get('bathrooms')
            new_property.single_bed = request.POST.get('single')
            new_property.double_bed = request.POST.get('double')
            new_property.king_bed = request.POST.get('king')
            new_property.queen_bed = request.POST.get('queen')
            new_property.num_review = request.POST.get('num_review')
            new_property.price = request.POST.get('price')
            new_property.amenities = request.POST.get('amenities')
            new_property.rating = request.POST.get('rating')
            new_property.cleaning_fee = request.POST.get('cleaning_fee')
            ###### image
            new_property.save()
            response['msg'] = 'Property infomation saved'
        except Exception as e:

            response['msg'] = 'Request failed to get %s.'%e
        return JsonResponse(response)

