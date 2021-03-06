
from django.urls import path,include
from .views import *
from django.conf.urls import url
app_name = 'foodchain'
urlpatterns = [

    path('dishes/', DishLstView.as_view(), name='dishlist'),
    path('places/', PlaceListView.as_view(),name='places'),
    path('restaurent/', RestListView.as_view(),name='restorents'),
    path('dishes/<int:pk>/', DishDetailedView.as_view(),name='dishdetails'),
    path('place/<int:pk>/', PlaceDetailedView.as_view(),name='placedetails'),
    path('restaurent/<int:pk>/', RestDetailedView.as_view(),name='restaurentDetails'),
    path('customer/<int:pk>/', CustomerDetailedView.as_view(),name='customerdet'),
    path('dishorder/<int:pk>/', order_create, name='dishcreate'),
    path('restorder/<int:pk>/', rest_create, name='restcreate'),
    path('signup/', signup,name='signup1'),
    path('', homepage, name='homein'),
    path('customercreate/<int:pk>', customerCreate, name='customercreate'),
    path('dishitemcreate/', dish_item_add, name='dishitemcreate'),
    path('restaurantprofile/<int:pk>/', RestaurantProfile.as_view(), name='restaurantprofile'),
    path('restorderslist/<int:pk>/', rest_order_list, name='restaurentorderlist'),
    path('restdishlist/<int:pk>/',rest_item_list,name='restitemlist'),
    path('restdishedit/<int:pk>/', rest_edit_dish, name='restdishedit'),
    path('order_cancel_customer/<pk>',deleteorder,name='dishitemdelete'),
    #path('dishitemcreate1/',dish_item_add,name='dishitemcreate1'),
    path('edit_rest_prof/<int:pk>/',rest_edit_profile,name='rest_edit_profile'),
    path('edit_customer_prof/<int:pk>/',cust_edit_profile,name='cust_edit_profile'),
    path('dishitemdetails/<int:pk>/', DishItemDetail.as_view(), name='dish_item_details'),

]

