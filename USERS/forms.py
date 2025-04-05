from django import forms
from django.contrib.auth.forms import UserCreationForm, get_user_model
Users = get_user_model()
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Users
        fields = ('email', 'first_name', 'last_name', 'phone', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput()
        self.fields['password2'].widget = forms.PasswordInput()
