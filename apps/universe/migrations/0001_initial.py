# Generated by Django 3.0.5 on 2020-04-19 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UniverseUser',
            fields=[
                ('ID', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='ID')),
                ('dpw', models.CharField(max_length=200, verbose_name='PSW')),
            ],
            options={
                'verbose_name': 'UniverseUser',
                'verbose_name_plural': 'UniverseUser',
                'db_table': 'UniverseUser1',
            },
        ),
    ]