from django.forms import ModelForm
from .models import ToduModel


class CreateToduFormsModel(ModelForm):
    class Meta:
        model = ToduModel
        exclude = ['created_at', 'task_status']
