
from requests import request
from rest_framework import serializers
from .models import Run


class RunSerializer(serializers.ModelSerializer):
    is_owner = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()

    def get_created_at(self, obj):
        return obj.created_at.strftime("%d %b %Y")
    

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Run
        fields = [
            'id', 'owner',  'is_owner', 'race', 'created_at'
        ]
