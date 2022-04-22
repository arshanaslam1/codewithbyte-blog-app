from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.forms.widgets import NumberInput
from .models import User
from .utils.validators import age_validator
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, SetPasswordForm


class AccountUpdateForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'First name',
               'class': 'uk-input uk-form-large uk-border-rounded',
               }))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Lastname',
               'class': 'uk-input uk-form-large uk-border-rounded',
               }))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'placeholder': 'Email',
               'class': 'uk-input uk-form-large uk-border-rounded',
               }))
    username = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Username',
               'class': 'uk-input uk-form-large uk-border-rounded',
               }))
    date_of_birth = forms.DateField(widget=NumberInput(
        attrs={'type': 'date',
               'class': 'uk-input uk-form-large uk-border-rounded',
               }),
        validators=[age_validator])

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'date_of_birth']


class AccountRegisterForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'First name',
               'class': 'uk-input uk-form-large uk-border-rounded',
               }))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Lastname',
               'class': 'uk-input uk-form-large uk-border-rounded',
               }))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'placeholder': 'Email',
               'class': 'uk-input uk-form-large uk-border-rounded',
               }))
    username = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Username',
               'class': 'uk-input uk-form-large uk-border-rounded',
               }))
    date_of_birth = forms.DateField(widget=NumberInput(
        attrs={'type': 'date',
               'class': 'uk-input uk-form-large uk-border-rounded',
               }),
        validators=[age_validator])
    password1 = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={'placeholder': 'Password',
               'class': 'uk-input uk-form-large uk-border-rounded',
               'type': 'password',
               }))
    password2 = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={'placeholder': 'Confirm Password',
               'class': 'uk-input uk-form-large uk-border-rounded',
               'type': 'password',
               }))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'date_of_birth', 'password1', 'password2']


class AccountLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Username',
               'required': True,
               'autofocus': True,
               'class': 'uk-input uk-form-large uk-border-rounded',
               }))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Password',
                   'required': True,
                   'class': 'uk-input uk-form-large uk-border-rounded',
                   'type': 'password',
                   }))
    remember_me = forms.BooleanField(required=False, widget=forms.CheckboxInput(
        attrs={'class': 'text-left inline_label', 'placeholder': 'Password', 'required': True}))


class AccountPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(AccountPasswordResetForm, self).__init__(*args, **kwargs)

    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'placeholder': 'Your email address',
               'class': 'uk-input uk-form-large uk-border-rounded',
               }))

    def clean_email(self):
        email = self.cleaned_data['email']
        if not User.objects.filter(email__iexact=email, is_active=True).exists():
            msg = "There is no user registered with the specified E-Mail address."
            self.add_error('email', msg)
        return email


class AccountPasswordResetConfirmForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(AccountPasswordResetConfirmForm, self).__init__(*args, **kwargs)

    new_password1 = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={'placeholder': 'New Password',
               'class': 'uk-input uk-form-large uk-border-rounded'
               }))
    new_password2 = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={'placeholder': 'Confirm New Password',
               'class': 'uk-input uk-form-large uk-border-rounded',
               }))


class AccountPasswordChangeForm(PasswordChangeForm):

    old_password = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={'placeholder': 'Old password',
               'class': 'uk-input uk-form-large uk-border-rounded',
               "autofocus": True
               }))
    new_password1 = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={'placeholder': 'New Password',
               'class': 'uk-input uk-form-large uk-border-rounded',
               }))
    new_password2 = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={'placeholder': 'Confirm New Password',
               'class': 'uk-input uk-form-large uk-border-rounded',
               }))


