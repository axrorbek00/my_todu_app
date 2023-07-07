from django.db import models
from django.contrib.auth.models import AbstractUser


class UsersModel(AbstractUser):
    img = models.ImageField(upload_to='users/', default='/static/main/imge/user_icon.jpg')
