from django.db.models import Count
from rest_framework import generics, filters
from main.privilege import IsOwerOrReadOnly
from .models import Run
from django_filters.rest_framework import DjangoFilterBackend
from .serializer import RunSerializer


class RunList(generics.ListCreateAPIView):
    queryset = Run.objects.all()
    serializer_class = RunSerializer
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]


class RunDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwerOrReadOnly]
    serializer_class = RunSerializer
    queryset = Run.objects.all()
