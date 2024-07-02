# Generated by Django 5.0.6 on 2024-07-02 08:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0002_alter_booking_package'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='package',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookings.package'),
        ),
    ]
