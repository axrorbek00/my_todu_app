# Generated by Django 4.2.2 on 2023-07-05 05:17

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todu', '0002_todumodel_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todumodel',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
