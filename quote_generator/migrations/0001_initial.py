# Generated by Django 3.1a1 on 2020-05-31 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('author', models.CharField(max_length=35)),
                ('content', models.CharField(max_length=100)),
            ],
        ),
    ]
