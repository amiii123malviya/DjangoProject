# Generated by Django 5.0.6 on 2024-05-16 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_query'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Password',
            field=models.CharField(max_length=300),
        ),
    ]
