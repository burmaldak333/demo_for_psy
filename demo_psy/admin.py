from django.contrib import admin
from .models import Psychologist, Service, Package

@admin.register(Psychologist)
class PsychologistAdmin(admin.ModelAdmin):
    pass

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')

@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_popular')