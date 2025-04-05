from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import CreateView
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView

from .forms import CustomUserCreationForm
# Create your views here.
User = get_user_model()

class RegisterView(CreateView):
    model = User
    template_name = 'USERS/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Akkountingiz yaratildi!")
        return response

    def form_invalid(self, form):
        messages.error(self.request, "Akkount yaratishda xatolik!")
        return super().form_invalid(form)

class CustomLoginView(LoginView):
    template_name = 'USERS/login.html'
    def get_success_url(self):
        return reverse_lazy('home')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Tizimga Muvaffaqiyatli kirdingiz!")
        return response


