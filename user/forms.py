from django import forms
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm
)


from .models import CustomUser,UserProfile,Post,Tag 

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


class ProfileUpdateForm(forms.ModelForm):
    """
    CustomUser modelidagi ma'lumotlarni tahrirlash uchun form
    """

    first_name= forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Ismingiz'
        })
    )

    last_name=forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Familiyangiz'
        })
    )

    phone_number=forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={
            'class':'form-input',
            'placeholder': '+998 94 136 52 92'
        })
    )

    avatar=forms.ImageField(
        required=False,
        widget=forms.FileInput(attrs={
            'class':'form-file',
            'accept':'image/*'
        }) 
        )


    class Meta:
        model = CustomUser
        fields= ['first_name','last_name','phone_number','avatar']



class UserProfileUpdateForm(forms.ModelForm):
    """
    UserProfile modelidagi ma'lumotlarni tahrirlsh uchun form
    """

    bio = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'class':'form-input',
            'placeholder':'O\'zingiz haqida yozing...',
            'rows': 4
        })
    )

    website = forms.URLField(
        required=False,
        widget=forms.URLInput(attrs={
            'class':'form-input',
            'placeholder':'https://example.com',
        })
    )

    class Meta:
        model = UserProfile
        fields = ['bio','website']


class PostForm(forms.ModelForm):
    title = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={
            'class':'form-input',
            'placeholder':'Post sarlavhasi...'
        })
    )
    content = forms.CharField(
        widget=forms.Textarea(attrs={
            'class':'form-input',
            'placeholder':'Post mazmuni...',
            'rows':8
        })
    )
    image = forms.ImageField(
        required=False,
        widget=forms.FileInput(attrs={
            'class':'form-title',
            'accept':'image/*'
        })
    )

    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        required = False,
        widget=forms.CheckboxSelectMultiple(attrs={'class':'tag-checkbox'})
    )
    
    class Meta:
        model = Post
        fields = ['title','content','image','tags']


