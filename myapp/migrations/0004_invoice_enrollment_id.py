# Generated by Django 3.2.8 on 2021-10-25 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_remove_invoice_enrollment_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='enrollment_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.enrollment'),
        ),
    ]
