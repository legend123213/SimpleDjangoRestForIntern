# Generated by Django 4.1 on 2023-08-26 20:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_person_user_alter_person_birthdate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='user',
        ),
    ]
