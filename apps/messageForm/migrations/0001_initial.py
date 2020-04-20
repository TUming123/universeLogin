# Generated by Django 3.0.5 on 2020-04-20 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MessageUser',
            fields=[
                ('ID', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='ID')),
                ('dpw', models.CharField(max_length=200, verbose_name='PSW')),
            ],
            options={
                'verbose_name': 'MessageUser1',
                'verbose_name_plural': 'MessageUser1',
                'db_table': 'MessageUser1',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('MID', models.CharField(max_length=50, verbose_name='MID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False, verbose_name='Mail')),
                ('address', models.CharField(max_length=100, verbose_name='Address')),
                ('message', models.TextField(verbose_name='Address')),
                ('date', models.CharField(max_length=50, verbose_name='Date')),
            ],
            options={
                'verbose_name': 'Message',
                'verbose_name_plural': 'Message',
                'db_table': 'Message1',
                'unique_together': {('MID', 'date')},
            },
        ),
    ]