from django.forms import ModelForm
from .models import ToduModel


class EditToduModelForm(ModelForm):
    class Meta:
        model = ToduModel
        fields = ['task_name', 'description']


class CreateToduFormsModel(ModelForm):
    class Meta:
        model = ToduModel
        exclude = ['created_at', 'task_status']
