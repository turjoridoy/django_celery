from django.urls import path
from django.contrib import admin
from app.views import index


urlpatterns = [
    path("", index),
    path('admin/', admin.site.urls),
]
