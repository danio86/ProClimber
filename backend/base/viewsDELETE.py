# from django.shortcuts import render
# from django.http import JsonResponse
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated, IsAdminUser #IsAuthenticated is for logged in users
# from .products import products
# from .models import Product
# from .serializers import ProductSerializer, UserSerializer, UserSerializerWithToken

# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
# from rest_framework_simplejwt.views import TokenObtainPairView

# from django.contrib.auth.models import User
# from django.contrib.auth.hashers import make_password
# from rest_framework import status



# class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
#     def validate(self, attrs):
#         data = super().validate(attrs)

#         serializer = UserSerializerWithToken(self.user).data #self.user is the user that is logged in
#         for key, val in serializer.items():
#             data[key] = val
#             # this genarates a token for the user that is logged in
#             # in restframework interface, we can see the token generated for the user
#             # with all the user details


#         # data['username'] = self.user.username
#         # data['email'] = self.user.email
#         # data['name'] = self.user.name
#         # data['is_staff'] = self.user.is_staff
        

#         return data
    
# class MyTokenObtainPairView(TokenObtainPairView):
#     serializer_class = MyTokenObtainPairSerializer


# @api_view(['POST'])
# def registerUser(request):
#     data = request.data #request.data is the data that is sent in the request
#     # print('data:', data)
#     try:
#         user = User.objects.create(
#             first_name = data['name'],
#             username = data['email'],
#             email = data['email'],
#             password = make_password(data['password']) #make_password is a function that hashes the password
#         )
#         serializer = UserSerializerWithToken(user, many=False) #many=False means we are serializing a single user
#         return Response(serializer.data)
#     except:
#         message = {'Error detail': 'User with this email already exists'}
#         return Response(message, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def getUserProfile(request):
#     user = request.user
#     serializer = UserSerializer(user, many=False) #many=False means we are serializing a single user
#     return Response(serializer.data)


# @api_view(['GET'])
# @permission_classes([IsAdminUser])
# def getUsers(request):
#     users = User.objects.all()
#     serializer = UserSerializer(users, many=True)
#     return Response(serializer.data)


# @api_view(['GET'])
# def getProducts(request):
#     products = Product.objects.all()
#     serializer = ProductSerializer(products, many=True) #many=True means we are serializing multiple products
#     return Response(serializer.data)



# @api_view(['GET'])
# def getProduct(request, pk):
#     product = Product.objects.get(_id=pk)
#     serializer = ProductSerializer(product, many=False)#many=False means we are serializing a single product
#     return Response(serializer.data)