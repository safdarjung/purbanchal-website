from django.contrib import admin
from .models import Service, Testimonial

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_featured', 'created_at')
    list_filter = ('is_featured',)
    search_fields = ('title', 'description')

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'is_active', 'created_at')
    list_filter = ('is_active',)
    search_fields = ('name', 'content')
