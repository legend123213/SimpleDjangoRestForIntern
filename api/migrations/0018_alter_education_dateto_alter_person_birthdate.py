# Generated by Django 4.1 on 2023-09-10 19:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_education_describtionofwork'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='DateTo',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='BirthDate',
            field=models.DateField(default=datetime.date(2005, 9, 10)),
        ),
    ]
