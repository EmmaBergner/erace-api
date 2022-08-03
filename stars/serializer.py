from turtle import update
from requests import request
from rest_framework import serializers
from .models import Star


class StarSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()


    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Star
        fields = [
            'id', 'owner', 'race', 'created_at', 'is_owner', 
        ]
