# Generated by Django 4.0.4 on 2022-05-01 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='categoyes',
            new_name='categories',
        ),
    ]
