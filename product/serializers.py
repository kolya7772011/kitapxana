from rest_framework import serializers
from .models import BookModel,AvtorModel

class AvtorModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvtorModel
        fields = ('full_name', 'about', 'birthday', 'country')


class BookModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookModel
        fields = ('name', 'page', 'price', 'year', 'avtor')        