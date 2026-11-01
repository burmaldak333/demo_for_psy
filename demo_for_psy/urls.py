from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # <--- ВОТ ЭТА СТРОКА ДОЛЖНА БЫТЬ
    path('', include('demo_psy.urls')),
]