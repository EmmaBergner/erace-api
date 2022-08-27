from django.db.models import Count
from rest_framework import generics, filters, permissions
from main.privilege import IsOwerOrReadOnly
from .models import Race
from django_filters.rest_framework import DjangoFilterBackend
from .serializer import RaceSerializer


class RaceList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Race.objects.all()
    serializer_class = RaceSerializer
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]

    filterset_fields = [
        'runs__owner__profile',
        'stars__owner__profile'
    ]

    search_fields = [
        'country',
    ]


class RaceDetail(generics.RetrieveUpdateAPIView):
    permission_classes = [IsOwerOrReadOnly]
    serializer_class = RaceSerializer
    queryset = Race.objects.all()
