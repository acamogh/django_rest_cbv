from rest_framework import serializers
from .models import Design


class DesignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Design

class DesignCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Design
        fields=['tag_name','theme_name','image_url','slug']

class DesignUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Design
        fields=['tag_name','theme_name','image_url','slug']


