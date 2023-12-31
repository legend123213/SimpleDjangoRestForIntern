# Generated by Django 4.1 on 2023-08-18 18:22

import api.models
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('FullName', models.CharField(max_length=20)),
                ('BirthDate', models.DateField(default=datetime.date(2005, 8, 18))),
                ('Email', models.EmailField(max_length=254, primary_key=True, serialize=False, unique=True)),
                ('PhoneNumber', models.IntegerField()),
                ('SelfDescribtion', models.TextField()),
                ('Street', models.CharField(max_length=50)),
                ('City', models.CharField(max_length=50)),
                ('Country', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=15)),
                ('Rate', models.IntegerField(validators=[api.models.RateValidator])),
            ],
            options={
                'db_table': 'Skill',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NameOfProject', models.CharField(max_length=50)),
                ('Description', models.TextField()),
                ('Link', models.URLField()),
                ('PersonId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.person')),
            ],
            options={
                'db_table': 'Project',
            },
        ),
        migrations.AddField(
            model_name='person',
            name='Skills',
            field=models.ManyToManyField(to='api.skill'),
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NameOfCompany', models.CharField(max_length=30)),
                ('Street', models.CharField(max_length=50)),
                ('City', models.CharField(max_length=50)),
                ('Country', models.CharField(max_length=50)),
                ('Role', models.CharField(max_length=20)),
                ('DescribtionOfWork', models.TextField()),
                ('DateFrom', models.DateField(blank=True)),
                ('DateTo', models.DateField(blank=True)),
                ('Email', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='api.person')),
            ],
            options={
                'db_table': 'Experience',
            },
        ),
    ]
