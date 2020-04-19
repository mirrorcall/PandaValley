import datetime
import decimal
from django.db.models import Q, Count
from django.http import JsonResponse
from django.views.generic.base import View
from django.contrib.gis.geos import GEOSGeometry
from .models import Property, Inspection, Booking, Reviews
from ..user.models import UserProfile, WishList
from django.core.mail import send_mail


class AddProperty(View):
    def post(self, request):
        response = {}
        response = {}
        #print(request.POST)
        #print(request.FILES)
        try:
            try:
                prop_id = request.POST.get('property_id')
                new_property = Property.objects.get(pk=prop_id)
            except:
                new_property = Property()
            # can not just write new_property.host = request.POST.get('email')
            new_property.host = UserProfile.objects.get(email=request.POST.get('email'))
            new_property.title = request.POST.get('title')
            # user = UserProfile.objects.get(email=host).first_name
            new_property.host_name = UserProfile.objects.get(email=new_property.host).first_name
            new_property.suburb = request.POST.get('suburb')
            new_property.street = request.POST.get('street')
            new_property.postcode = request.POST.get('postcode')
            latitude = request.POST.get('latitude')
            longitude = request.POST.get('longitude')
            ##new changes
            point = f'POINT({latitude} {longitude})'
            new_property.latitude_longitude = GEOSGeometry(point, srid=4326)
            new_property.description = request.POST.get('description')
            new_property.guests = request.POST.get('guests')
            # room info
            new_property.amenities = request.POST.get('amenities')
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
                        # print(new_property.image.url)
                        new_property.save()
                        new_property.image_url = new_property.image.url
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
        #print(response)
        return JsonResponse(response)


class DeletePropertyView(View):
    def post(self, request):
        response = {}
        try:
            prop_id = request.POST.get('property_id')
            prop = Property.objects.get(pk=prop_id)
            bookings = Booking.objects.filter(host=prop).exclude(state='canceled').values()
            state = True
            if bookings.exists():
                for each in bookings.iterator():
                    if each['end_date'] > datetime.datetime.now().date():
                        state = False
                        break
            if state:
                prop.is_deleted = state
                prop.save()
                response['code'] = 0
                response['msg'] = 'The property has been deleted.'
            else:
                response['code'] = 1
                response['msg'] = 'There still have bookings not finished, can not delete the property.'
        except Exception as e:
            response['code'] = 127
            response['msg'] = 'Internal server failure. ' + str(e)
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
            prop_type = request.GET.get('property_type', None)
            page = int(page)
            res = Property.objects \
                .filter(Q(street__icontains=location) | Q(title__icontains=location) | Q(suburb__icontains=location)) \
                .order_by(order).distinct()

            if prop_type:
                res = res.filter(property_type=prop_type)
            if guests:
                res = res.filter(guests__gte=guests)
            if bed:
                res = res.filter(bedrooms__gte=bed)
            if bathroom:
                res = res.filter(bathrooms__gte=bathroom)
            if max_price:
                res = res.filter(price__lte=max_price)
            if min_price:
                res = res.filter(price__gte=min_price)

            result = []
            #print('res', type(res))
            # res <class 'django.db.models.query.QuerySet'>
            res = res.values()
            if res.exists():
                for each in res.iterator():
                    # temp = {}
                    if not Booking.objects.filter(host=each['id']) \
                            .filter(Q(start_date__lte=datetime.date(end_date[2], end_date[1], end_date[0])),
                                    Q(end_date__gte=datetime.date(start_date[2], start_date[1], start_date[0])))\
                            .exclude(state='canceled'):
                        temp = dict()
                        temp['property_id'] = each['id']
                        temp['title'] = each['title']  # prop.title
                        temp['image'] = each['image_url']
                        temp['bedrooms'] = each['bedrooms']
                        temp['bathrooms'] = each['bathrooms']
                        temp['guests'] = each['guests']
                        temp['price'] = each['price']
                        temp['suburb'] = each['suburb']
                        temp['street'] = each['street']
                        ##new changes
                        temp['rating'] = each['rating']

                        if user:
                            temp['saved'] = False
                            state = WishList.objects.filter(user=user, property=each['id'])
                            if state:
                                temp['saved'] = True

                        result.append(temp)

            response['code'] = 0
            response['msg'] = 'Return search information.'
            response['total'] = len(result)
            #print(result,'result')
            if page == 1:
                response['body'] = result[0:8]
            else:
                if len(result) - 8 * page > 0:
                    response['body'] = result[8 * (page - 1):8 * (page - 1) + 8]
                else:
                    response['body'] = result[8 * (page - 1):len(result) + 1]
        except Exception as e:
            response['code'] = 127
            response['msg'] = 'Internal server failure. ' + str(e)

        return JsonResponse(response)


class VerifyReserveView(View):
    def post(self, request):
        response = {}
        try:
            # property id
            prop_id = request.POST.get('property')
            start_date = request.POST.get('start_date')
            end_date = request.POST.get('end_date')
            start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y")
            end_date = datetime.datetime.strptime(end_date, "%d/%m/%Y")
            response['state'] = False
            period = end_date - start_date
            period = period.days
            # check if avaiable
            if not Booking.objects.filter(host=prop_id) \
                    .filter(Q(start_date__lte=end_date), Q(end_date__gte=start_date))\
                    .exclude(state='canceled'):
                response['state'] = True  # true can book
            res = dict()
            prop = Property.objects.get(pk=prop_id)

            res['period'] = period
            res['total_cost'] = prop.price * period + prop.cleaning_fee
            response['code'] = 0
            response['msg'] = 'Return booking state.'
            response['body'] = res
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
            user = request.GET.get('email',None)
            prop = Property.objects.get(pk=prop_id)
            #print(datetime.datetime.strptime(end_date,"%d/%m/%Y"))
            period = datetime.datetime.strptime(end_date,"%d/%m/%Y")- \
                     datetime.datetime.strptime(start_date, "%d/%m/%Y")
            period = period.days
            ##images
            # if automatically injected
            images = []
            if prop.image.name:
                images.append(prop.image.url)
                img = Inspection.objects.filter(property=prop_id)
                if img.exists():
                    for i in range(len(img)):
                        images.append(img[i].image.url)
            else:
                images.append(prop.image_url)
                img = Inspection.objects.filter(property=prop_id)
                if img.exists():
                    for i in range(len(img)):
                        images.append(img[i].image_url)
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
            #It's Lat/Lon on 4326.
            res['latitude'] = prop.latitude_longitude[0]
            res['longitude'] = prop.latitude_longitude[1]
            s = False
            if user:
                state = WishList.objects.filter(user=user, property=prop_id)
                #print(state)
                if state:
                    s = True
            res['saved'] = s
            response['code'] = 0
            response['msg'] = 'Return search information.'
            response['body'] = res
        except Exception as e:
            response['code'] = 127
            response['msg'] = 'Internal server failure. ' + str(e)
        #print(response)
        return JsonResponse(response)


class ShowReviewsView(View):
    def get(self, request):
        response = {}
        try:
            prop_id = request.GET.get('property')
            result = Reviews.objects.filter(property=prop_id).order_by('-id').values()
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
            booking = request.POST.get('booking_id')
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
            # change the booking status
            record = Booking.objects.get(pk=booking)
            record.state = 'completed'
            record.save()
            #print(record.state)

            response['code'] = 0
            response['msg'] = 'Save review information.'
        except Exception as e:
            response['code'] = 127
            response['msg'] = 'Internal server failure. ' + str(e)

        return JsonResponse(response)


class ShowWishListView(View):
    def get(self, request):
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
                    temp['image'] = prop.image_url
                    temp['wishlist_id'] = each[0]
                    temp['rating'] = prop.rating
                    result.append(temp)

            response['code'] = 0
            response['msg'] = 'Return wish list information.'
            response['body'] = result
        except Exception as e:
            response['code'] = 127
            response['msg'] = 'Internal server failure. ' + str(e)
        #print(response)
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
            # print(email,prop_id,start_date,end_date)
            start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y")
            end_date = datetime.datetime.strptime(end_date, "%d/%m/%Y")
            # NEW BOOKING
            response['state'] = False
            if not Booking.objects.filter(host=prop_id) \
                    .filter(Q(start_date__lte=end_date), Q(end_date__gte=start_date))\
                    .exclude(state='canceled'):
                response['state'] = True  # true can book
                new_booking = Booking()
                new_booking.guest = UserProfile.objects.get(pk=email)
                new_booking.host = Property.objects.get(pk=prop_id)
                new_booking.start_date = start_date
                new_booking.end_date = end_date
                new_booking.days = period
                new_booking.total_cost = decimal.Decimal(cost)
                new_booking.state = 'uncompleted'
                new_booking.save()
            response['msg'] = 'Return booking state.'
            response['code'] = 0
            if response['state'] and UserProfile.objects.get(email=email):
                # encryption
                mail_title = 'Thank you for your booking with PandaValley'
                mail_body = \
                    f"Dear {new_booking.guest.first_name},\n\n" + \
                    f"We are pleased to inform you that your booking at {new_booking.host.street} is confirmed.\n\n" + \
                    f"Your check-in : {new_booking.start_date.date()}\n" + \
                    f"Your checkout : {new_booking.end_date.date()}\n\n" + \
                    "Reservation details:\n\n" + \
                    f"Room type: {new_booking.host.property_type}\nGuests: {new_booking.host.guests}\n" + \
                    f"Days: {new_booking.days}\nTotal cost: ${new_booking.total_cost}\n\n" + \
                    "Sincerely awaiting your visit."
                send_state = send_mail(mail_title, mail_body, 'pdvalley.official@gmail.com', [email])
                #print(send_state)
                response['code'] = 0
                response['msg'] = 'Sent email,new booking saved'
            else:
                response['code'] = 1
                response['msg'] = 'The booking dates are not available.'
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
    ### user side
    def get(self, request):
        response = {}
        try:
            email = request.GET.get('email')
            # order by latest
            bookings = Booking.objects.filter(guest=email).order_by('-id').values()
            res = dict()
            res['uncompleted'] = []
            res['checkedin'] = []
            res['completed'] = []
            res['uncommented'] = []
            res['canceling'] = []
            res['canceled'] = []

            if bookings.exists():
                for each in bookings.iterator():
                    temp = dict()
                    temp['booking_id'] = each['id']
                    temp['property_id'] = each['host_id']
                    temp['start_date'] = each['start_date']
                    temp['end_date'] = each['end_date']
                    temp['days'] = each['days']
                    temp['total_cost'] = each['total_cost']
                    current_time = datetime.datetime.now().date()

                    # print(temp['state'])
                    if each['state'] not in ['completed', 'canceling', 'canceled']:
                        if current_time < each['start_date']:
                            each['state'] = 'uncompleted'
                        elif current_time < each['end_date']:
                            each['state'] = 'checked in'
                        else:
                            each['state'] = 'uncommented'
                    prop = Property.objects.get(pk=each['host_id'])
                    temp['title'] = prop.title
                    # if automatically injected
                    temp['bedrooms'] = prop.bedrooms
                    temp['bathrooms'] = prop.bathrooms
                    temp['guests'] = prop.guests
                    temp['host_name'] = prop.host_name
                    temp['contact'] = prop.host.telephone
                    temp['image'] = prop.image_url
                    temp['street'] = prop.street
                    temp['suburb'] = prop.suburb
                    temp['price'] = prop.price
                    # deal with checked in
                    if each['state'] == 'checked in':
                        res['checkedin'].append(temp)
                    else:
                        res[each['state']].append(temp)
                    # print('333333333333333')

            response['msg'] = 'Return wish list information.'
            response['body'] = res
            #print(res)
        except Exception as e:
            response['code'] = 127
            response['msg'] = 'Internal server failure. ' + str(e)
        return JsonResponse(response)


class ShowHostBookingView(View):
    # show bookings from users
    def get(self, request):
        response = {}
        try:
            #print(request)
            host = request.GET.get('property_id')
            prop = Property.objects.get(pk=host)
            res = Booking.objects.filter(host=prop).order_by('-id').values()
            result = []
            if res.exists():
                for each in res.iterator():
                    result.append(each)
            response['body'] = result
            response['msg'] = 'Applied for cancel booking.'
        except Exception as e:
            response['code'] = 127
            response['msg'] = 'Internal server failure. ' + str(e)
        return JsonResponse(response)


class ShowHostPropertyView(View):
    # show property
    def get(self, request):
        response = {}
        #print(request)
        try:
            host = request.GET.get('email')
            # order by latest
            prop = Property.objects.filter(host=host).order_by('-id').values()
            res = []
            if prop.exists():
                for each in prop.iterator():
                    temp = dict()
                    # prop = Property.objects.get(pk=each['host_id'])
                    temp['property_id'] = each['id']
                    temp['title'] = each['title']  # prop.title
                    temp['image'] = each['image_url']
                    temp['bedrooms'] = each['bedrooms']
                    temp['bathrooms'] = each['bathrooms']
                    temp['guests'] = each['guests']
                    temp['price'] = each['price']
                    temp['suburb'] = each['suburb']
                    temp['street'] = each['street']
                    temp['postcode'] = each['postcode']
                    # temp['longitude'] = prop.host.email
                    temp['property_type'] = each['property_type']
                    temp['description'] = each['description']
                    temp['email'] = each['postcode']
                    temp['single_bed'] = each['single_bed']
                    temp['double_bed'] = each['double_bed']
                    temp['queen_bed'] = each['queen_bed']
                    temp['king_bed'] = each['king_bed']
                    temp['amenities'] = each['amenities']
                    temp['cleaning_fee'] = each['cleaning_fee']
                    images = []
                    prop = Property.objects.get(pk=each['id'])
                    if prop.image.name:
                        images.append(prop.image.url)
                        img = Inspection.objects.filter(property=each['id'])
                        if img.exists():
                            for i in range(len(img)):
                                images.append(img[i].image.url)
                    else:
                        images.append(prop.image_url)
                        img = Inspection.objects.filter(property=each['id'])
                        if img.exists():
                            for i in range(len(img)):
                                images.append(img[i].image_url)
                    res.append(temp)
                    temp['image'] = images
            response['code'] = 0
            response['msg'] = 'Return My Property information.'
            response['body'] = res
        except Exception as e:
            response['code'] = 127
            response['msg'] = 'Internal server failure. ' + str(e)
        return JsonResponse(response)


class ApplyRefundView(View):
    def post(self, request):
        response = {}
        try:
            booking = request.POST.get('booking_id')
            record = Booking.objects.get(pk=booking)
            record.state = 'canceling'
            record.save()
            # print(record.state)
            response['code'] = 0
            response['msg'] = 'Applied for cancel booking.'
        except Exception as e:
            response['code'] = 127
            response['msg'] = 'Internal server failure. ' + str(e)
        return JsonResponse(response)


class AgreeRefundView(View):
    #after canceled send the email
    def post(self, request):
        response = {}
        try:
            booking = request.POST.get('booking_id')
            record = Booking.objects.get(pk=booking)
            record.state = 'canceled'
            #record.is_deleted = True
            record.save()
            #print(record)
            mail_title = 'Your booking has been canceled.'
            mail_body = \
                f"Dear {record.guest.first_name},\n\n" + \
                f"We are pleased to inform you that your booking at {record.host.street} has been canceled.\n\n" + \
                f"Your check-in : {record.start_date}\n" + \
                f"Your checkout : {record.end_date}\n\n" + \
                "Reservation details:\n\n" + \
                f"Room type: {record.host.property_type}\nGuests: {record.host.guests}\n" + \
                f"Days: {record.days}\nRefund: ${record.total_cost}\n\n"
            send_state = send_mail(mail_title, mail_body, 'pdvalley.official@gmail.com', [record.guest.email])
            # print(record.state)
            response['code'] = 0
            response['msg'] = 'The booking has been canceled.'
        except Exception as e:
            response['code'] = 127
            response['msg'] = 'Internal server failure. ' + str(e)
        return JsonResponse(response)


class ShowNearbyPropertyView(View):
    def get(self, request):
        response = {}
        try:
            # LocationsNearMe = Property.objects.filter(latitude__gte=(the minimal lat from distance()),
            #                   latitude__lte = (the minimal lat from distance()),
            user = request.GET.get('email')
            prop_id = request.GET.get('property_id')
            start_date = request.GET.get('start_date')
            end_date = request.GET.get('end_date')
            start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y")
            end_date = datetime.datetime.strptime(end_date, "%d/%m/%Y")
            prop = Property.objects.get(pk=prop_id)
            #within the range
            res = Property.objects.filter(latitude_longitude__distance_lte=(prop.latitude_longitude, 0.02)).exclude(pk=prop_id).values()
            result = []
            count = 0
            if res.exists():
                for each in res.iterator():
                    if count == 5:
                        break
                    if not Booking.objects.filter(host=each['id']) \
                            .filter(Q(start_date__lte=end_date),
                                    Q(end_date__gte=start_date))\
                            .exclude(state='canceled'):
                        temp = {}
                        temp['property_id'] = each['id']
                        temp['title'] = each['title']  # prop.title
                        temp['image'] = each['image_url']
                        temp['bedrooms'] = each['bedrooms']
                        temp['bathrooms'] = each['bathrooms']
                        temp['guests'] = each['guests']
                        temp['price'] = each['price']
                        temp['suburb'] = each['suburb']
                        temp['street'] = each['street']
                        temp['rating'] = each['rating']
                        # wishlist
                        s = False
                        if user:
                            state = WishList.objects.filter(user=user, property=each['id'])
                            if state:
                                s = True
                        temp['saved'] = s
                        result.append(temp)
                        count += 1

            response['code'] = 0
            response['msg'] = 'Return My Property information.'
            response['body'] = result
            # response['body'] = res
        except Exception as e:
            response['code'] = 127
            response['msg'] = 'Internal server failure. ' + str(e)
        return JsonResponse(response)


class RefuseRefundView(View):
    def post(self, request):
        response = {}
        try:
            booking = request.POST.get('booking_id')
            record = Booking.objects.get(pk=booking)
            record.state = 'uncompleted'
            record.save()
            mail_title = 'Your application for canceling the booking has been refused.'
            mail_body = \
                f"Dear {record.guest.first_name},\n\n" + \
                f"We are pleased to inform you that your application for canceling booking at {record.host.street} has been refused.\n\n" + \
                f"Your check-in : {record.start_date}\n" + \
                f"Your checkout : {record.end_date}\n\n" + \
                "Reservation details:\n\n" + \
                f"Room type: {record.host.property_type}\nGuests: {record.host.guests}\n" + \
                f"Days: {record.days}\nCost: ${record.total_cost}\n\n"
            send_state = send_mail(mail_title, mail_body, 'pdvalley.official@gmail.com', [record.guest.email])
            response['code'] = 0
            response['msg'] = 'The application for canceling booking has been refused.'
        except Exception as e:
            response['code'] = 127
            response['msg'] = 'Internal server failure. ' + str(e)
        return JsonResponse(response)


class RecommendedPropertyView(View):
    def get(self, request):
        response = {}
        try:
            # res = Property.objects.all().order_by('-rating')[:10].values()
            res = Property.objects.all().order_by('-rating')[:8].values()
            result = []
            if res.exists():
                for each in res.iterator():
                    temp = {}
                    temp['property_id'] = each['id']
                    temp['title'] = each['title']  # prop.title
                    temp['image'] = each['image_url']
                    temp['bedrooms'] = each['bedrooms']
                    temp['bathrooms'] = each['bathrooms']
                    temp['guests'] = each['guests']
                    temp['price'] = each['price']
                    temp['suburb'] = each['suburb']
                    temp['street'] = each['street']
                    temp['rating'] = each['rating']
                    result.append(temp)
            response['code'] = 0
            response['msg'] = 'Return recommended Property information.'
            response['body'] = result
            # response['body'] = res
        except Exception as e:
            response['code'] = 127
            response['msg'] = 'Internal server failure. ' + str(e)
        return JsonResponse(response)


class PropertyOverView(View):
    def get(self, request):
        response = {}
        try:
            res = Property.objects.all().values('property_type').annotate(total=Count('property_type'))
            result = []
            for i in range(len(res)):
                result.append(res[i])
            response['code'] = 0
            response['msg'] = 'Return property type overview information.'
            response['body'] = result
            # response['body'] = res
        except Exception as e:
            response['code'] = 127
            response['msg'] = 'Internal server failure. ' + str(e)
        return JsonResponse(response)
