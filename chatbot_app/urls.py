from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name="login"),
    path('register/', views.register_view, name="register"),
    path('chatbot/', views.chatbot_view, name="chatbot"),
    path('new_chat/', views.new_chat, name="new_chat"),
    path('logout/', views.logout_view, name="logout"),
]