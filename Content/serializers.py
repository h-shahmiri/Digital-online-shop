from rest_framework.serializers import ModelSerializer , HyperlinkedModelSerializer
from rest_framework import serializers
from .models import Item


class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = ('kinds','name','id')


class ItemListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ('url','name','id')