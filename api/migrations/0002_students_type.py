# Generated by Django 5.0 on 2025-01-03 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='type',
            field=models.CharField(choices=[('ERKAK', 'ERKAK'), ('AYOL', 'AYOL')], default='api', max_length=10),
            preserve_default=False,
        ),
    ]
