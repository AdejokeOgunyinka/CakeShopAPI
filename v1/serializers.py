from rest_framework import serializers
from .models import Customer, Cake, Order, Recipe


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id','firstname', 'lastname', 'home_address', 'phone_number']


class CakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cake
        fields = ['id','name', 'price', 'description']


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['cake', 'ingredients']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['customer', 'cake', 'quantity']
