from rest_framework import serializers
from .models import usersInfo,product,orders
class RegisterSerializer(serializers.ModelSerializer):
    class Meta():
        model=usersInfo
        fields='__all__'
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=20)

class ProductSerializer(serializers.ModelSerializer):
    class Meta():
        model=product
        fields='__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta():
        model=orders
        fields=['productid','quantity',]

class UserBasedOrderSerializers(serializers.ModelSerializer):
    class Meta():
        model=orders
        fields='__all__'