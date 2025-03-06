# Generated by Django 5.1.5 on 2025-03-02 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dormitory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dorm',
            name='approval_status',
            field=models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending', max_length=10),
        ),
    ]
