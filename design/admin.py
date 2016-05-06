from django.contrib import admin
from .models import Design

# Register your models here.
class DesignAdmin(admin.ModelAdmin):
    list_display=['tag_name','theme_name','user']
    prepopulated_fields = {"slug": ("tag_name",)}

    # class Met



admin.site.register(Design,DesignAdmin)