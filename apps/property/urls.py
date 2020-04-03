from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'add_property', views.AddProperty.as_view()),
    re_path(r'search_property', views.SearchPropertyView.as_view()),
    re_path(r'varify_booking', views.VerifyReserveView.as_view()),
    re_path(r'show_property', views.ShowPropertyView.as_view()),
    re_path(r'show_reviews', views.ShowReviewsView.as_view()),
    re_path(r'add_review', views.AddReviewView.as_view()),
    re_path(r'show_wishlist', views.ShowWishListView.as_view()),
    re_path(r'delete_wishlist', views.DeleteWishListView.as_view()),
    re_path(r'add_wishlist', views.AddWishListView.as_view()),
    re_path(r'show_reviews', views.ReserveView.as_view()),
    re_path(r'delete_booking', views.DeleteBookingView.as_view()),
    re_path(r'show_booking', views.ShowBookingView.as_view())
]


