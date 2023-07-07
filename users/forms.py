from django import forms
from django.core.validators import ValidationError
from .models import UsersModel


class LoginForms(forms.Form):
    username = forms.CharField(max_length=20, widget=forms.TextInput(attrs={
        'placeholder': 'username'
    }))
    password = forms.CharField(max_length=16, widget=forms.PasswordInput())


# class LoginForms(forms.ModelForm):
#     class Meta:
#         model = UsersModel
#         fields = ['username', 'password']
#         widgets = {
#             'username': forms.TextInput(attrs={
#                 'placeholder': 'username'
#             }),
#             'password': forms.PasswordInput(attrs={
#                 'placeholder': 'password'
#             })
#         }


class RegistrationModelForm(forms.Form):
    username = forms.CharField(max_length=20, min_length=3, widget=forms.TextInput(attrs={
        'placeholder': 'username'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'youremailname@gmail.com'
    }))
    first_name = forms.CharField(max_length=25)
    last_name = forms.CharField(max_length=25, required=False)
    password = forms.CharField(max_length=16, min_length=6, widget=forms.PasswordInput)
    canfirm_password = forms.CharField(max_length=16, min_length=6, widget=forms.PasswordInput)

    def clean_canfirm_password(self):
        print(self.cleaned_data)
        if self.cleaned_data['password'] != self.cleaned_data['canfirm_password']:
            raise ValidationError('Parollar birxil emas !')
        return self.cleaned_data
