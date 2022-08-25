from turtle import update
from requests import request
from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    #owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    owner_username = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_created_at(self, obj):
        return obj.created_at.strftime("%d %b %Y")
    
    def get_updated_at(self, obj):
        return obj.updated_at.strftime("%d %b %Y")

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_owner_username(self, obj):
        request = self.context['request']
        return obj.owner.username

    class Meta:
        model = Comment
        fields = [
            'id', 'owner', 'owner_username', 'is_owner', 'race', 'created_at',
             'updated_at', 'text', 'image'
        ]
