# Generated by Django 4.2.2 on 2023-07-04 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_usersmodel_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersmodel',
            name='img',
            field=models.ImageField(default='/static/main/imge/user_icon.jpg', upload_to='users/'),
        ),
    ]
