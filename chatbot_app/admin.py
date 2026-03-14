from django.contrib import admin
from .models import User, ChatHistory

admin.site.register(User)
admin.site.register(ChatHistory)