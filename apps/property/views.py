import datetime
from django.db.models import Q
from django.http import JsonResponse
from django.views.generic.base import View

from .models import Property, Inspection, Booking

from ..user.models import UserProfile


class AddProperty(View):
    def post(self, request):
        response = {}
        print(request.POST)
        print(request.FILES)
        try:
            new_property = Property()
            # can not just write new_property.host = request.POST.get('email')
            new_property.host = UserProfile.objects.get(email=request.POST.get('email'))
            new_property.title = request.POST.get('title')
            # user = UserProfile.objects.get(email=host).first_name
            new_property.host_name = UserProfile.objects.get(email=new_property.host).first_name
            new_property.suburb = request.POST.get('suburb')
            new_property.street = request.POST.get('street')
            new_property.postcode = request.POST.get('postcode')
            # new_property.latitude = request.POST.get('latitude')
            # new_property.longitude = request.POST.get('longitude')
            new_property.description = request.POST.get('description')
            new_property.guests = request.POST.get('guests')
            # room info
            # new_property.amenities = request.POST.get('amenities')
            new_property.room_type = request.POST.get('room_type')
            new_property.bathrooms = request.POST.get('bathroom')
            new_property.bedrooms = request.POST.get('bedrooms')
            new_property.single_bed = request.POST.get('single_bed')
            new_property.double_bed = request.POST.get('double_bed')
            new_property.queen_bed = request.POST.get('queen_bed')
            new_property.king_bed = request.POST.get('king_bed')
            new_property.price = request.POST.get('price')
            # image
            images = request.FILES.getlist('image')
            if not images:
                response['code'] = 1
                response['msg'] = 'Lacking of inspection images/views'
            else:
                for i in range(len(images)):
                    #print(images[i], type(images[i]))
                    if i == 0:
                        new_property.image = images[i]
                        print(new_property.image.url)
                        new_property.save()
                        new_property.imageUrl = new_property.image.url
                        new_property.save()
                    else:
                        #new_Inspection = Inspection.objects.get(property_id=new_property.id)
                        new_Inspection = Inspection()
                        new_Inspection.property = Property.objects.get(pk=new_property.id)
                        new_Inspection.image = images[i]
                        new_Inspection.save()
                response['code'] = 0
                response['msg'] = 'Property information saved.'
        except Exception as e:
            response['code'] = 127
            response['msg'] = 'Internal server failure. ' + str(e)
        print(response)
        return JsonResponse(response)


class SearchPropertyView(View):
    def get(self, request):
        print(request.GET)
        response = {}
        try:
            location = request.GET.get('location')
            location = location.replace('number_of_people=', '')
            print('==========', location)
            start_date = request.GET.get('start_date').split('/')
            end_date = request.GET.get('end_date').split('/')
            start_date = [int(i) for i in start_date]
            end_date = [int(i) for i in end_date]
            bed = request.GET.get('bedrooms', None)
            bathroom = request.GET.get('bathrooms', None)
            guests = request.GET.get('number_of_people', None)
            print(guests)
            print(type(guests))
            order = request.GET.get('order', '-rating')
            min_price = request.GET.get('min_price', None)
            max_price = request.GET.get('max_price', None)
            page = request.GET.get('page', 1)
            page = int(page)
            res = Property.objects \
                .filter(Q(street__icontains=location) | Q(title__icontains=location) | Q(suburb__icontains=location)) \
                .order_by(order).distinct()

            if guests:
                res = res.filter(guests__gte=guests)
            elif bed:
                res = res.filter(bedrooms__gte=bed)
            elif bathroom:
                res = res.filter(bathrooms__gte=bathroom)
            elif max_price:
                res = res.filter(price__lte=max_price)
            elif min_price:
                res = res.filter(price__gte=min_price)

            result = []
            res = res.values()
            if res.exists():
                for each in res.iterator():
                    # temp = {}
                    if not Booking.objects.filter(host=each['id']) \
                            .filter(Q(start_date__lte=datetime.date(end_date[2], end_date[1], end_date[0])),
                                    Q(end_date__gte=datetime.date(start_date[2], start_date[1], start_date[0]))):
                        result.append(each)
            #add paginator  later check but works
            # result_paginator = Paginator(result, page)
            # try:
            #     result_post = result_paginator.page(page)
            # except PageNotAnInteger:
            #     result_post = result_paginator.page(8)
            # except EmptyPage:
            #     result_post = result_paginator.page(result_paginator.num_pages)
            response['code'] = 0
            response['msg'] = 'Return search information.'
            if len(result)%8 == 0:
                response['total'] = len(result)//8
            else:
                response['total'] = len(result) // 8 + 1
            if page == 1:
                response['body'] = result[0:8]
            else:
                if 8*page > len(result):
                    response['body'] = result[8*(page-1):8*(page-1)+8]
                else:
                    response['body'] = result[8*(page-1):len(result)+1]
        except Exception as e:
            response['code'] = 127
            response['msg'] = 'Internal server failure. ' + str(e)
        print(response)
        return JsonResponse(response)