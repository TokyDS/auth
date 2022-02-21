from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView

from .models import Post


class PostListView(LoginRequiredMixin, generic.ListView):
    model = Post


class PostDetailView(LoginRequiredMixin, PermissionRequiredMixin, generic.DetailView):
    permission_required = "polls.view_post"
    # Если просто запрещать челам без прав видеть эту страницу(выдаст 403 ошибку)
    model = Post


def home(request):
    return render(request, "polls/home.html")


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
