# Generated by Django 4.1.7 on 2023-05-10 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('sname', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('sage', models.IntegerField()),
            ],
        ),
    ]
