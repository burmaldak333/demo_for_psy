from django.urls import path, include

urlpatterns = [
    path('', include('demo_psy.urls')), # <--- Здесь demo_psy, а не main
]