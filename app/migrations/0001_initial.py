# Generated by Django 3.2 on 2021-04-26 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('mobile', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=35)),
                ('message', models.TextField()),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
