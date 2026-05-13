from django import forms
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm
)


from .models import CustomUser

#     RRGISTER FORM

class RegisterForm(UserCreationForm):

    class Meta:
        model = CustomUser

        fields = [
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'avatar',
            'password1',
            'password2',
        ]


class LoginForm(AuthenticationForm):

    username = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'Email kiriting'
            }
        )
    )


