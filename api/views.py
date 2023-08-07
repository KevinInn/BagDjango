from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from django.shortcuts import redirect

from .models import Product
from .models import Picture
from .models import Comment
from .models import Member
from .models import Cart
from .models import Orders

from .serializers import ProductSerializer
from .serializers import PictureSerializer
from .serializers import CommentSerializer
from .serializers import MemberSerializer
from .serializers import CartSerializer
from .serializers import OrdersSerializer

# Create your views here.
@api_view(['GET'])
def getProducts(request, pId):
    product = Product.objects.get(pId=pId)
    serializer = ProductSerializer(product, many=False)#serializer
    return Response(serializer.data)

@api_view(['GET'])
def getPictures(request, pId):
    pictures = get_object_or_404(Picture, pk=pId)
    serializer = PictureSerializer(pictures)#serializer
    return Response(serializer.data)

@api_view(['GET'])
def getComments(request, pId):
    comments = Comment.objects.filter(pId=pId)
    serializer = CommentSerializer(comments, many=True)#serializer
    return Response(serializer.data)

@api_view(['GET'])
def getMember(request, mId):
    member = Member.objects.filter(mId=mId)
    serializer = MemberSerializer(member, many=True)#serializer
    return Response(serializer.data)

@api_view(['POST'])
def addToCart(request):
    data = request.data
    pId = data['pId']
    mId = data['mId']
    product = Product.objects.get(pId=pId)
    member = Member.objects.get(mId=mId)
    cart = Cart.objects.create(
        pId = product,
        mId = member,
        cartTime = data['cartTime']
    )
    serializer = CartSerializer(cart, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def goCheck(request):
    data = request.data
    bagId = data['bagId']#bagId是一個存了數字的Array
    request.session['checkList'] = bagId
    print()
    return redirect('/#/checkout')

@api_view(['POST'])
def getCheck(request):
    bagIds = request.session.get('checkList', [])
    return Response(bagIds)

@api_view(['POST'])
def updateOrder(request):
    data = request.data
    pId = data['pId']
    mId = data['mId']
    product = Product.objects.get(pId=pId)
    member = Member.objects.get(mId=mId)
    order = Orders.objects.create(
        mId = member,
        pId = product,
        payment = data['payment'],
        order_time = data['order_time'],
        duration = data['duration'],
        address = data['address'],
        state = data['state'],
        startTime = data['startTime'],
        endTime = data['endTime']
    )
    serializer = OrdersSerializer(order, many=False)
    return redirect('/#/')