# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .products import products
from .models import Product, Order, OrderItem, ShippingAddress, Review
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User



class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)
    _id = serializers.SerializerMethodField(read_only=True)
    isAdmin = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = ['id', '_id', 'username', 'isAdmin', 'email', 'name'] #return only these fields

    def get__id(self, obj):
        return obj.id
    
    def get_isAdmin(self, obj):
        return obj.is_staff

    def get_name(self, obj):
        name = obj.first_name
        if name == '':
            name = obj.email
        return name
    

    
class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = ['id', '_id', 'username', 'isAdmin', 'email', 'name', 'token'] #return only these fields

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'




class ProductSerializer(serializers.ModelSerializer): #serializers.ModelSerializer is a class
    reviews = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = '__all__' #return all the fields

    def get_reviews(self, obj):
        reviews = obj.review_set.all() #review_set is a reverse relationship
        serializer = ReviewSerializer(reviews, many=True)
        return serializer.data
    


class ShippingAddressSerializer(serializers.ModelSerializer): #serializers.ModelSerializer is a class
    class Meta:
        model = ShippingAddress
        fields = '__all__' #return all the fields



class OrderItemSerializer(serializers.ModelSerializer): #serializers.ModelSerializer is a class
    class Meta:
        model = OrderItem
        fields = '__all__' #return all the fields



class OrderSerializer(serializers.ModelSerializer): #serializers.ModelSerializer is a class
    orderItems = serializers.SerializerMethodField(read_only=True)
    shippingAddress = serializers.SerializerMethodField(read_only=True)
    user = serializers.SerializerMethodField(read_only=True)
    # paymentMethod = serializers.SerializerMethodField(read_only=True)
    # taxPrice = serializers.SerializerMethodField(read_only=True)
    # shippingPrice = serializers.SerializerMethodField(read_only=True)
    # totalPrice = serializers.SerializerMethodField(read_only=True)
    # isPaid = serializers.SerializerMethodField(read_only=True)
    # paidAt = serializers.SerializerMethodField(read_only=True)
    # isDelivered = serializers.SerializerMethodField(read_only=True)
    # deliveredAt = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Order
        fields = '__all__' #return all the fields

    def get_orderItems(self, obj):
        items = obj.orderitem_set.all() #orderitem_set is a reverse relationship
        serializer = OrderItemSerializer(items, many=True)
        return serializer.data
    
    def get_shippingAddress(self, obj):
        try:
            address = ShippingAddressSerializer(obj.shippingaddress, many=False).data #shippingaddress is a reverse relationship
        except:
            address = False
        return address
    
    def get_user(self, obj):
        user = obj.user
        serializer = UserSerializer(user, many=False)
        return serializer.data
    
    # def get_paymentMethod(self, obj):
    #     return obj.paymentMethod
    
    # def get_taxPrice(self, obj):
    #     return obj.taxPrice
    
    # def get_shippingPrice(self, obj):
    #     return obj.shippingPrice
    
    # def get_totalPrice(self, obj):
    #     return obj.totalPrice
    
    # def get_isPaid(self, obj):
    #     return obj.isPaid
    
    # def get_paidAt(self, obj):
    #     return obj.paidAt
    
    # def get_isDelivered(self, obj):
    #     return obj.isDelivered
    
    # def get_deliveredAt(self, obj):
    #     return obj.deliveredAt