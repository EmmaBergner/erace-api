from django.db.models import Count
from rest_framework import generics, filters
from main.privilege import IsOwerOrReadOnly
from .models import Comment
from django_filters.rest_framework import DjangoFilterBackend
from .serializer import CommentSerializer


class CommentList(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]


class CommentDetail(generics.RetrieveUpdateAPIView):
    permission_classes = [IsOwerOrReadOnly]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
