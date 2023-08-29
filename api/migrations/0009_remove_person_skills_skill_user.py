# Generated by Django 4.1 on 2023-08-26 21:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_remove_person_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='Skills',
        ),
        migrations.AddField(
            model_name='skill',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='api.person'),
        ),
    ]