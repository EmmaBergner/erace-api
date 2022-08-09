from turtle import update
from requests import request
from rest_framework import serializers
from .models import Race
from django.contrib.humanize.templatetags.humanize import datetime


class RaceSerializer(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    #date = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    # def get_date(self, obj):
    #     return obj.date.strftime("%A %d %B %Y, %H:%M")

    def get_created_at(self, obj):
        return obj.date.strftime("%d %b %Y")
    
    def get_updated_at(self, obj):
        return obj.date.strftime("%d %b %Y")

    class Meta:
        model = Race
        fields = [
            'id', 'owner', 'name', 'distance', 'country', 'date', 'website', 'created_at', 'updated_at',
            'is_owner', 
        ]
