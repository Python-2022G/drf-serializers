# Generated by Django 4.2.4 on 2023-08-09 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(default=''),
        ),
    ]