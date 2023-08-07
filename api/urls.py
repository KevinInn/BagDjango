from django.urls import path
from . import views

urlpatterns = [
    path('product/<int:pId>', views.getProducts, name="products"),
    path('picture/<int:pId>', views.getPictures, name="pictures"),
    path('comment/<int:pId>', views.getComments, name="comments"),
    path('member/<int:mId>', views.getMember, name="members"),
    path('member/addToCart/', views.addToCart, name="addToCart"),
    path('member/updateOrder/', views.updateOrder, name="updateOrder"),
    path('goCheck/', views.goCheck, name="goCheck"),
    path('getCheck/', views.getCheck, name="getCheck")
]