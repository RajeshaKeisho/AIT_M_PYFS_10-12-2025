from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    discount_price = serializers.SerializerMethodField()
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'discount_price', 'price','published_date']

    def get_discount_price(self, obj):
        return obj.price * 0.90
    
    def validate_price(self, value):
        if value < 100:
            raise serializers.ValidationError("Price must be greater than 100")
        return value
    
    def validate(self, data):
        if data['title'] == "Free Book" and data['price'] > 0:
            raise serializers.ValidationError("Free Book must have price 0")
        return data
    
