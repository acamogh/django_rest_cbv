from django.shortcuts import render,HttpResponse
from rest_framework import generics,authentication,viewsets,permissions
from .models import Design
from .serializers import DesignSerializer,DesignCreateSerializer
from rest_framework.permissions import (AllowAny,IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly)

# Create your views here.
def home (request):
    return HttpResponse('hello')

class PostListAPIView(generics.ListAPIView):

    queryset = Design.objects.all()
    serializer_class = DesignSerializer
    lookup_field = 'slug'

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
    lookup_field = 'theme_name'

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

class PostDeleteAPIView(generics.DestroyAPIView):
    queryset = Design.objects.all()
    serializer_class = DesignSerializer
    lookup_field = 'theme_name'