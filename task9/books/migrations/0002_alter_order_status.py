# Generated by Django 4.2.9 on 2024-01-04 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('pending', 'pending'), ('confirmed', 'confirmed'), ('delivered', 'delivered'), ('cancelled', 'cancelled')], default='pending', max_length=100),
        ),
    ]
