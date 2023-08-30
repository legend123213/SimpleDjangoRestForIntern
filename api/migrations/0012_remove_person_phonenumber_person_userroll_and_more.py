# Generated by Django 4.1 on 2023-08-30 19:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_remove_person_skills_experience_email_person_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='PhoneNumber',
        ),
        migrations.AddField(
            model_name='person',
            name='UserRoll',
            field=models.CharField(default='roll', max_length=40),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='person',
            name='BirthDate',
            field=models.DateField(default=datetime.date(2005, 8, 30)),
        ),
    ]
