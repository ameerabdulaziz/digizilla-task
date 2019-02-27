from django import forms
from django.contrib.auth.forms import PasswordResetForm, UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class UserRegisterForm(UserCreationForm, forms.ModelForm):
    first_name = forms.CharField(required=True, widget=forms.TextInput)
    last_name = forms.CharField(required=True, widget=forms.TextInput)
    email = forms.CharField(required=True, widget=forms.EmailInput)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')


class EmailValidationOnForgotPassword(PasswordResetForm):
    def clean_email(self):
        email = self.cleaned_data['email']
        if not User.objects.filter(email__iexact=email, is_active=True).exists():
            raise ValidationError("There is no user registered with the specified email address!")
        return email
