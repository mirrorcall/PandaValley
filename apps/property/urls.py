from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'add_property', views.AddProperty.as_view()),
    re_path(r'search_property', views.SearchPropertyView.as_view()),
    ###new changes
    re_path(r'edit_booking', views.VerifyReserveView.as_view()),
    re_path(r'show_property', views.ShowPropertyView.as_view()),
    re_path(r'show_reviews', views.ShowReviewsView.as_view()),
    re_path(r'add_review', views.AddReviewView.as_view()),
    re_path(r'show_wishlist', views.ShowWishListView.as_view()),
    re_path(r'delete_wishlist', views.DeleteWishListView.as_view()),
    re_path(r'add_wishlist', views.AddWishListView.as_view()),
    re_path(r'reserve', views.ReserveView.as_view()),
    re_path(r'delete_booking', views.DeleteBookingView.as_view()),
    re_path(r'show_booking', views.ShowBookingView.as_view()),
    re_path(r'my_property', views.ShowHostPropertyView.as_view()),
    re_path(r'canceling', views.ApplyRefundView.as_view()),
    re_path(r'canceled', views.AgreeRefundView.as_view()),
    re_path(r'my_property_booking', views.ShowHostBookingView.as_view())
]
