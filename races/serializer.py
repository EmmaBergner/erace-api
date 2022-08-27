import time
from requests import request
from rest_framework import serializers
from stars.models import Star
from runs.models import Run
from .models import Race
from django.contrib.humanize.templatetags.humanize import datetime


class RaceSerializer(serializers.ModelSerializer):
    is_owner = serializers.SerializerMethodField()
    owner_username = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()
    star_id = serializers.SerializerMethodField()
    run_id = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_created_at(self, obj):
        return obj.created_at.strftime("%d %b %Y")

    def get_updated_at(self, obj):
        return obj.updated_at.strftime("%d %b %Y")

    def get_star_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            star = Star.objects.filter(
                owner=user, race=obj).first()
            return star.id if star else None
        return None

    def get_run_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            run = Run.objects.filter(
                owner=user, race=obj).first()
            return run.id if run else None
        return None

    def get_owner_username(self, obj):
        request = self.context['request']
        return obj.owner.username

    class Meta:
        model = Race
        fields = [
            'id', 'owner', 'owner_username', 'name', 'distance', 
            'country', 'date', 'website', 'created_at', 'updated_at',
             'is_owner', 'star_id', 'run_id',
        ]
