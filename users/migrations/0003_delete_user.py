# Generated by Django 4.1.4 on 2022-12-15 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_rename_birthdate_user_birthday_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
