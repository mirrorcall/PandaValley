from django.http import JsonResponse
from django.views.generic.base import View
from django.db.models import Q
from ..property.models import Property, Inspection, Booking
from ..user.models import UserProfile


# from ..user.models import
# Create your views here.

class Search(View):
    def get(self, request):
        response = {}
        try:
            location = request.GET.get('location')
            start_date = request.GET.get('start_data')
            end_date = request.GET.get('end_data')
            # if not then default to be 0
            price = request.GET.get('price', None)
            bed = request.GET.get('bedrooms', None)
            bathroom = request.GET.get('bathrooms', None)
            guests = request.GET.get('number_of_people', None)
            res = Property.objects.filter(Q(address__icontains=location)
                                          | Q(title__icontains=location) | Q(suburb__icontains=location))

            # Property.objects.select_related()
            if guests:
                res = res.filter(guests__gte=guests)
            elif bed:
                res = res.filter(bedrooms__gte=bed)
            elif bathroom:
                res = res.filter(bathrooms__gte=bathroom)
            # result = []
            res = res.values()
            if res.exists():
                for each in res:
                    print(each)

                # res = res.filter(Q(Booking__start_date__gt=end_date)|Q(Booking__end_data__lt=start_date))
                # for prop in res:
                #
                #     bookings = Booking.objects.filter(pk=prop.id)
                #     if bookings.exists():
                #         for each in bookings.iterator():
                #             if each.

            response['code'] = 0
            response['msg'] = 'Return search information.'
            response['body'] = res
        except Exception as e:
            response['code'] = 127
            response['msg'] = 'Internal server failure. ' + str(e)

        return JsonResponse(response)
