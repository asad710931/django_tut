# Generated by Django 5.1.5 on 2025-01-27 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_icon', models.CharField(max_length=100)),
                ('service_title', models.CharField(max_length=100)),
                ('service_das', models.TextField()),
            ],
        ),
    ]
