# Generated by Django 4.1 on 2023-08-30 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_remove_person_phonenumber_person_userroll_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='PhoneNumber',
            field=models.CharField(default='09_________', max_length=30),
            preserve_default=False,
        ),
    ]
