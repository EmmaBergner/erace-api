from turtle import update
from requests import request
from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    race = serializers.ReadOnlyField(source = 'race.id')


    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Comment
        fields = [
            'id', 'owner', 'text', 'race', 'created_at', 'updated_at',
            'is_owner',  'image', 
        ]
