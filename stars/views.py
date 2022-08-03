from django.db.models import Count
from rest_framework import generics, filters
from main.privilege import IsOwerOrReadOnly
from .models import Star 
from django_filters.rest_framework import DjangoFilterBackend
from .serializer import StarSerializer


class StarList(generics.ListAPIView):
    queryset = Star.objects.all()
    serializer_class = StarSerializer
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]


class StarDetail(generics.RetrieveUpdateAPIView):
    permission_classes = [IsOwerOrReadOnly]
    serializer_class = StarSerializer
    queryset = Star.objects.all()
