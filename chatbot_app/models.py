from django.db import models

class User(models.Model):

    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=200)


class ChatHistory(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    question = models.TextField()

    response = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)