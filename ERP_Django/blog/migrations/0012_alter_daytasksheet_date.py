# Generated by Django 4.1.6 on 2023-02-22 15:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_alter_daytasksheet_shop'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daytasksheet',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, unique=True),
        ),
    ]
