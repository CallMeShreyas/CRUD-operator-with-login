# Generated by Django 4.0 on 2022-01-16 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superuser', '0005_employee_epoints'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='epoints',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
