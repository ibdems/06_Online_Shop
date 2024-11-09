from typing import Any
from django import forms
from django.contrib.auth.hashers import check_password
from admin_volt.forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from django.core.exceptions import ValidationError

from .utils.send_emails import send_mail_activation
from users.models import User

class CustomLoginForm(AuthenticationForm):
    def clean(self) -> dict[str, Any]:
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        try:
            user = User.objects.get(email=username)
        except User.DoesNotExist:
            raise ValidationError(
                "Email ou mot de pass invalid"
            )           
        
        if not user.is_active:
            send_mail_activation(user)
            raise ValidationError(
                "Votre compte n'est pas actif, consulter votre boite mail pour l'activer"
            )
        
        if not user.check_password(password):
            raise ValidationError(
                "Email ou mot de pass invalid"
            )
        self.user_cache = user
        
        return self.cleaned_data

class CustomCreateUserForm(RegistrationForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Cette adresse email existe deja.")
        return email

