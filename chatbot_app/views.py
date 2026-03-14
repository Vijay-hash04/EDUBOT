from django.contrib import messages
from django.shortcuts import render, redirect
from .models import User, ChatHistory
from .gemini_chatbot import get_bot_response
import markdown

# REGISTER
def register_view(request):

    if request.method == "POST":

        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect("register")

        User.objects.create(
            username=username,
            email=email,
            password=password
        )

        messages.success(request, "Registered Successfully!")
        return redirect("login")

    return render(request, "register.html")


# LOGIN
def login_view(request):

    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]

        try:
            user = User.objects.get(username=username, password=password)

            request.session["user_id"] = user.id

            messages.success(request, "Logged in Successfully!")
            return redirect("chatbot")

        except User.DoesNotExist:
            messages.error(request, "Invalid username or password")

    return render(request, "login.html")


# CHATBOT
def chatbot_view(request):

    if "user_id" not in request.session:
        return redirect("login")

    user = User.objects.get(id=request.session["user_id"])

    if request.method == "POST":

        question = request.POST["question"]

        response = get_bot_response(question)

        formatted_response = markdown.markdown(response)

        ChatHistory.objects.create(
            user=user,
            question=question,
            response=formatted_response
        )

    chats = ChatHistory.objects.filter(user=user).order_by("id")

    return render(request, "chatbot.html", {"chats": chats})


# NEW CHAT (clear previous chat view)
def new_chat(request):

    if "user_id" not in request.session:
        return redirect("login")

    return redirect("chatbot")


# LOGOUT
def logout_view(request):

    request.session.flush()

    messages.success(request, "Logged out successfully!")

    return redirect("login")