import datetime
import decimal

from django.db.models import Q
from django.http import JsonResponse
from django.views.generic.base import View

from .models import Property, Inspection, Booking, Reviews

from ..user.models import UserProfile, WishList
#from django.forms.models import model_to_dict
from django.core.mail import send_mail
class AddProperty(View):
    def post(self, request):
        response = {}
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
            new_property.property_type = request.POST.get('property_type')
            new_property.bathrooms = request.POST.get('bathrooms')
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
                    # print(images[i], type(images[i]))
                    if i == 0:
                        new_property.image = images[i]
                        print(new_property.image.url)
                        new_property.save()
                        new_property.imageUrl = new_property.image.url
                        new_property.save()
                    else:
                        # new_Inspection = Inspection.objects.get(property_id=new_property.id)
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
        response = {}
        try:
            location = request.GET.get('location')
            user = request.GET.get('email', None)
            start_date = request.GET.get('start_date').split('/')
            end_date = request.GET.get('end_date').split('/')
            start_date = [int(i) for i in start_date]
            end_date = [int(i) for i in end_date]
            bed = request.GET.get('bedrooms', None)
            bathroom = request.GET.get('bathrooms', None)
            guests = request.GET.get('number_of_people', None)
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
            #print('res',type(res))
            #res <class 'django.db.models.query.QuerySet'>
            res = res.values()
            if res.exists():
                for each in res.iterator():
                    # temp = {}
                    if not Booking.objects.filter(host=each['id']) \
                            .filter(Q(start_date__lte=datetime.date(end_date[2], end_date[1], end_date[0])),
                                    Q(end_date__gte=datetime.date(start_date[2], start_date[1], start_date[0]))):
                        if user:
                            each['saved'] = False
                            state = WishList.objects.filter(user=user, property=each['id'])
                            if state:
                                each['saved'] = True
                        result.append(each)
            # add paginator  later check but works
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

        return JsonResponse(response)

############# you wenti ???????
class VerifyReserveView(View):
    def post(self, request):
        response = {}
        try:
            # property id
            prop_id = request.POST.get('property')
            start_date = request.POST.get('start_date')
            end_date = request.POST.get('end_date')
            print(datetime.datetime.strptime(start_date, "%d/%m/%Y"))
            start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y")
            end_date = datetime.datetime.strptime(end_date, "%d/%m/%Y")
            response['state'] = False
            # check if avaiable
            if not Booking.objects.filter(host=prop_id) \
                    .filter(Q(start_date__lte=end_date), Q(end_date__gte=start_date)):
                response['state'] = True # true can book
            response['msg'] = 'Return booking state.'
            response['code'] = 0
        except Exception as e:
            response['code'] = 127
            response['msg'] = 'Internal server failure. ' + str(e)

        return JsonResponse(response)


class ShowPropertyView(View):
    def get(self, request):
        response = {}
        try:
            # property id
            prop_id = request.GET.get('property')
            start_date = request.GET.get('start_date')
            end_date = request.GET.get('end_date')
            prop = Property.objects.get(pk=prop_id)
            print(datetime.datetime.strptime(end_date,"%d/%m/%Y"))
            period = datetime.datetime.strptime(end_date,"%d/%m/%Y")- \
                     datetime.datetime.strptime(start_date, "%d/%m/%Y")
            period = period.days
            ##images
            images = []
            images.append(prop.image.url)
            img = Inspection.objects.filter(property=prop_id)
            if img.exists():
                for i in range(len(img)):
                    images.append(img[i].image.url)
            res = dict()
            res['title'] = prop.title
            res['host_name'] = prop.host.first_name
            res['host_avatar'] = prop.host.avatar.url
            res['suburb'] = prop.suburb
            res['property_type'] = prop.property_type
            res['description'] = prop.description
            res['guests'] = prop.guests
            res['bedrooms'] = prop.bedrooms
            res['bathrooms'] = prop.bathrooms
            res['single_bed'] = prop.single_bed
            res['double_bed'] = prop.double_bed
            res['queen_bed'] = prop.queen_bed
            res['king_bed'] = prop.king_bed
            res['price'] = prop.price
            res['amenities'] = prop.amenities
            res['rating'] = prop.rating
            res['cleaning_fee'] = prop.cleaning_fee
            res['image'] = images
            res['period'] = period
            res['total_cost'] = period*prop.price + prop.cleaning_fee
            # res['num_review'] = prop.num_review
            # res['num_review'] = prop.num_review

            # x y on the google map
            # latitude = models.FloatField(default=0)
            # longitude = models.FloatField(default=0)

            response['code'] = 0
            response['msg'] = 'Return search information.'
            response['body'] = res
        except Exception as e:
            response['code'] = 127
            response['msg'] = 'Internal server failure. ' + str(e)
        print(response)
        return JsonResponse(response)


class ShowReviewsView(View):
    def get(self, request):
        response = {}
        try:
            prop_id = request.GET.get('property')
            result = Reviews.objects.filter(property=prop_id).values()
            response['code'] = 0
            response['msg'] = 'Return review information.'
            #print(type(result))
            if result.exists():
                res = [each for each in result.iterator()]
                response['body'] = res
            else:
                response['body'] = []
        except Exception as e:
            response['code'] = 127
            response['msg'] = 'Internal server failure. ' + str(e)

        return JsonResponse(response)


class AddReviewView(View):
    def post(self, request):
        response = {}
        try:
            prop_id = request.POST.get('property')
            user_id = request.POST.get('email')
            comment = request.POST.get('context')
            ## float
            rating = decimal.Decimal(request.POST.get('rating'))
            #print(type(rating))
            new_review = Reviews()
            new_review.property = Property.objects.get(pk=prop_id)
            new_review.user = UserProfile.objects.get(pk=user_id)
            new_review.context = comment
            new_review.username = new_review.user.first_name
            new_review.rating = rating
            new_review.property.rating = (new_review.property.num_review * new_review.property.rating + rating)\
                                         /(new_review.property.num_review + 1)
            new_review.property.num_review += 1
            new_review.save()
            new_review.property.save()

            response['code'] = 0
            response['msg'] = 'Save review information.'
        except Exception as e:
            response['code'] = 127
            response['msg'] = 'Internal server failure. ' + str(e)

        return JsonResponse(response)


class ShowWishListView(View):
    def get(self, request):
        # response = {}
        # try:
        #     email = request.GET.get('email')
        #     res = WishList.objects.filter(user=email).values()
        #     res = [each['property_id'] for each in res.iterator()]
        #     res = Property.objects.filter(id__in=res).values()
        #     res = [each for each in res]
        #     response['total'] = len(res)
        #     response['code'] = 0
        #     response['msg'] = 'Return wish list information.'
        #     response['body'] = res
        # except Exception as e:
        #     response['code'] = 127
        #     response['msg'] = 'Internal server failure. ' + str(e)
        # print(response)
        response = {}
        try:
            email = request.GET.get('email')
            res = WishList.objects.filter(user=email).values()
            # wishlist_id   property_id
            res = [(each['id'], each['property_id']) for each in res.iterator()]
            # res = [each['property_id'] for each in res.iterator()]
            result = []
            if res:
                for each in res:
                    temp = dict()
                    prop = Property.objects.get(pk=each[1])
                    temp['wishlist_id'] = each[0]
                    temp['property_id'] = prop.id
                    temp['title'] = prop.title
                    temp['host_name'] = prop.host.first_name
                    temp['guests'] = prop.guests
                    temp['bedrooms'] = prop.bedrooms
                    temp['bathrooms'] = prop.bathrooms
                    temp['price'] = prop.price
                    temp['image'] = prop.imageUrl
                    temp['wishlist_id'] = each[0]
                    result.append(temp)

            response['code'] = 0
            response['msg'] = 'Return wish list information.'
            response['body'] = result
        except Exception as e:
            response['code'] = 127
            response['msg'] = 'Internal server failure. ' + str(e)
        print(response)
        return JsonResponse(response)


class AddWishListView(View):
    def post(self, request):
        response = {}
        try:
            email = request.POST.get('email')
            prop = request.POST.get('property')
            new = WishList()
            new.user = UserProfile.objects.get(pk=email)
            new.property = Property.objects.get(pk=prop)
            new.save()
            response['code'] = 0
            response['msg'] = 'Added into wish list.'
        except Exception as e:
            response['code'] = 127
            response['msg'] = 'Internal server failure. ' + str(e)
        return JsonResponse(response)

#email
class DeleteWishListView(View):
    def post(self, request):
        response = {}
        try:
            #property_id
            temp = request.POST.get('wishlist_id')
            WishList.objects.get(pk=temp).delete()
            response['code'] = 0
            response['msg'] = 'Delete current property from wish list.'
        except Exception as e:
            response['code'] = 127
            response['msg'] = 'Internal server failure. ' + str(e)
        return JsonResponse(response)


class ReserveView(View):
    def post(self, request):
        response = {}
        try:
            email = request.POST.get('email')
            prop_id = request.POST.get('property_id')
            start_date = request.POST.get('start_date')
            end_date = request.POST.get('end_date')
            period = request.POST.get('period')
            cost = request.POST.get('total_cost')
            print(email,prop_id,start_date,end_date,period,cost)
            start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y")
            end_date = datetime.datetime.strptime(end_date, "%d/%m/%Y")
            # NEW BOOKING
            new_booking = Booking()
            new_booking.guest = UserProfile.objects.get(pk=email)
            new_booking.host = Property.objects.get(pk=prop_id)
            new_booking.start_date = start_date
            new_booking.end_date = end_date
            new_booking.days = period
            new_booking.total_cost = decimal.Decimal(cost)
            new_booking.save()
            response['code'] = 0
            response['msg'] = 'New booking saved.'

            if UserProfile.objects.get(email=email):
                # encryption
                mail_title = 'Thank you for your booking with PandaValley'
                mail_body = \
                    f"Dear {new_booking.guest.first_name},\n\n" +\
                    f"We are pleased to inform you that your booking at {new_booking.host.street},{new_booking.host.suburb} is confirmed.\n\n"+ \
                    f"Your check-in : {new_booking.start_date.date()}\n" +\
                    f"Your checkout : {new_booking.end_date.date()}\n\n" +\
                    "Reservation details:\n\n" +\
                    f"Room type: {new_booking.host.property_type}\nGuests: {new_booking.host.guests}\n"+\
                    f"Days: {new_booking.days}\nTotal cost: ${new_booking.total_cost}\n\n"+\
                    "Sincerely awaiting your visit."
                send_state = send_mail(mail_title, mail_body, 'pdvalley.official@gmail.com', [email])
                print(send_state)
                response['code'] = 0
                response['msg'] = 'Sent email.'
            response['code'] = 0
            response['msg'] = 'New booking saved.'
        except Exception as e:
            response['code'] = 127
            response['msg'] = 'Internal server failure. ' + str(e)
        return JsonResponse(response)


class DeleteBookingView(View):
    def post(self, request):
        response = {}
        try:
            booking_id = request.POST.get('booking_id')
            booking = Booking.objects.get(pk=booking_id)
            booking.is_deleted = True
            booking.save()
            response['code'] = 0
            response['msg'] = 'Delete current Booking information from My Booking.'
        except Exception as e:
            response['code'] = 127
            response['msg'] = 'Internal server failure. ' + str(e)
        return JsonResponse(response)


class ShowBookingView(View):
    def get(self, request):
        response = {}
        try:
            email = request.GET.get('email')
            #order by latest
            bookings = Booking.objects.filter(guest=email).order_by('-id').values()
            res = []
            if bookings.exists():
                for each in bookings.iterator():
                    temp = dict()
                    temp['booking_id'] = each['id']
                    temp['start_date'] = each['start_date']
                    temp['end_date'] = each['end_date']
                    temp['days'] = each['days']
                    temp['total_cost'] = each['total_cost']
                    prop = Property.objects.get(pk=each['host_id'])
                    temp['title'] = prop.title
                    temp['image'] = prop.imageUrl
                    temp['bedrooms'] = prop.bedrooms
                    temp['bathrooms'] = prop.bathrooms
                    temp['guests'] = prop.guests
                    temp['host_name'] = prop.host_name
                    temp['contact'] = prop.host.telephone
                    temp['email'] = prop.host.email
                    res.append(temp)

            response['msg'] = 'Return wish list information.'
            response['body'] = res
        except Exception as e:
            response['code'] = 127
            response['msg'] = 'Internal server failure. ' + str(e)
        return JsonResponse(response)


class ShowHostPropertyView(View):
    def get(self, request):
        response = {}
        print(request)
        try:
            host = request.GET.get('email')
            #order by latest
            prop = Property.objects.filter(host=host).values()
            res = []
            if prop.exists():
                for each in prop.iterator():
                    temp = dict()
                    #prop = Property.objects.get(pk=each['host_id'])
                    temp['property_id'] = each['id']
                    temp['title'] = each['title']#prop.title
                    temp['image'] = each['imageUrl']
                    temp['bedrooms'] = each['bedrooms']
                    temp['bathrooms'] = each['bathrooms']
                    temp['guests'] = each['guests']
                    temp['price'] = each['price']
                    res.append(temp)
            response['code'] = 0
            response['msg'] = 'Return My Property information.'
            response['body'] = res
        except Exception as e:
            response['code'] = 127
            response['msg'] = 'Internal server failure. ' + str(e)
        print(response)
        return JsonResponse(response)
