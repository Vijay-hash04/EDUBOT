from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # include app urls
    path('', include('chatbot_app.urls')),
]