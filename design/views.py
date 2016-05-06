from django.shortcuts import render,HttpResponse
from rest_framework import generics,authentication,viewsets,permissions
from rest_framework.filters import SearchFilter,OrderingFilter
from django.db.models import Q
from .models import Design
from .permissions import IsOwnerOrReadOnly
from .serializers import DesignSerializer,DesignCreateSerializer
from rest_framework.permissions import (AllowAny,IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly)


# Create your views here.
def home (request):
    return HttpResponse('hello')

# list
class PostListAPIView(generics.ListAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = DesignSerializer
    filter_backends = [SearchFilter, OrderingFilter] # api/?search=indian&ordering=theme_name&q=...
    search_fields=['tag_name','theme_name','theme_name','user__first_name']

    def get_queryset(self, *args, **kwargs):
        queryset_list = Design.objects.all()
        query = self.request.GET.get('q')
        print query
        if query:
            queryset_list = queryset_list.filter(
                Q(theme_name__icontains=query)|
                Q(tag_name__icontains=query)|
                Q(user__first_name=query)|
                Q(tag_name__icontains=query)

            ).distinct()
        return queryset_list

# create
class PostCreateAPIView(generics.CreateAPIView):
    queryset = Design.objects.all()
    serializer_class = DesignCreateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

#  detail
class PostDetailAPIView(generics.RetrieveAPIView):
    queryset = Design.objects.all()
    serializer_class = DesignSerializer
    lookup_field = 'theme_name'

# update
class PostUpdateAPIView(generics.RetrieveAPIView,generics.UpdateAPIView):
    queryset = Design.objects.all()
    serializer_class = DesignCreateSerializer
    permission_classes = [IsOwnerOrReadOnly]
    lookup_field = 'theme_name'

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

# delete
class PostDeleteAPIView(generics.RetrieveAPIView,generics.DestroyAPIView):
    queryset = Design.objects.all()
    serializer_class = DesignSerializer
    lookup_field = 'theme_name'