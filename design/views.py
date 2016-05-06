from django.shortcuts import render,HttpResponse
from rest_framework import generics,authentication,viewsets,permissions
from django.db.models import Q
from .models import Design
from .permissions import IsOwnerOrReadOnly
from .serializers import DesignSerializer,DesignCreateSerializer
from rest_framework.permissions import (AllowAny,IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly)


# Create your views here.
def home (request):
    return HttpResponse('hello')

class PostListAPIView(generics.ListAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = DesignSerializer

    def get_queryset(self, *args, **kwargs):
        queryset_list = Design.objects.all()
        query = self.request.GET.get('q')
        print query
        if query:
            queryset_list = queryset_list.filter(
                Q(theme_name__icontains=query)
            ).distinct()
        return queryset_list


class PostCreateAPIView(generics.CreateAPIView):
    queryset = Design.objects.all()
    serializer_class = DesignCreateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PostDetailAPIView(generics.RetrieveAPIView):
    queryset = Design.objects.all()
    serializer_class = DesignSerializer
    lookup_field = 'slug'

class PostUpdateAPIView(generics.RetrieveAPIView,generics.UpdateAPIView):
    queryset = Design.objects.all()
    serializer_class = DesignCreateSerializer
    permission_classes = [IsOwnerOrReadOnly]

    lookup_field = 'theme_name'


    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

class PostDeleteAPIView(generics.DestroyAPIView):
    queryset = Design.objects.all()
    serializer_class = DesignSerializer
    lookup_field = 'theme_name'