# Generated by Django 3.2.8 on 2021-10-25 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_invoice_enrollment_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='enrollment_id',
        ),
    ]
