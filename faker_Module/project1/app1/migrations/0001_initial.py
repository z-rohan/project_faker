# Generated by Django 4.0.5 on 2022-06-12 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('sid', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('address', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=40)),
            ],
        ),
    ]
