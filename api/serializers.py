from rest_framework.serializers import ModelSerializer
from .models import Product
from .models import Picture
from .models import Comment
from .models import Member
from .models import Cart
from .models import Orders
class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        
class PictureSerializer(ModelSerializer):
    class Meta:
        model = Picture
        fields = '__all__'

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class MemberSerializer(ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'
        
class CartSerializer(ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

class OrdersSerializer(ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'