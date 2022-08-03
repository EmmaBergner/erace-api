from django.db.models import Count
from rest_framework import generics, filters
from main.privilege import IsOwerOrReadOnly
from .models import Profile
from django_filters.rest_framework import DjangoFilterBackend
from .serializer import ProfileSerializer


class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]


class ProfileDetail(generics.RetrieveUpdateAPIView):
    permission_classes = [IsOwerOrReadOnly]
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
