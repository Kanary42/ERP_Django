# Generated by Django 4.1.6 on 2023-02-22 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_alter_daytasksheet_date'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='daytasksheet',
            unique_together={('date', 'shop')},
        ),
    ]
