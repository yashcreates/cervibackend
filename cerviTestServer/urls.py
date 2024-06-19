from django.contrib import admin
from django.urls import path, include  

urlpatterns = [
    path('admin/', include("admin.urls")),  # Include admin URLs directly
    path('auth/', include("authentication.urls")),  # Include authentication app URLs
    path('detection/', include("detection.urls")),  # Include detection app URLs
    path('requests/', include("request.urls")),  # Include request app URLs
    path('chats/', include("chat.urls")),  # Include chat app URLs
]
