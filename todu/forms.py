from django import forms
from .models import ToduModel


class EditToduModelForm(forms.ModelForm):
    class Meta:
        model = ToduModel
        fields = ['task_name', 'description']


class CreateToduFormsModel(forms.ModelForm):
    class Meta:
        model = ToduModel
        exclude = ['created_at', 'task_status']
