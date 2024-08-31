
from django.contrib import admin
from django.urls import path
from app01 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("chat/", views.chat),
    path('send/msg/', views.send_msg),
    path("get/msg/", views.get_msg),
]
