# Generated by Django 4.1.6 on 2023-02-22 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_rename_site_worksite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daytask',
            name='site',
            field=models.CharField(choices=[(1, 'LK1'), (2, 'LK2'), (3, 'LK3'), (4, 'Welding'), (5, 'Fitting'), (6, 'TS1620'), (7, 'FC'), (8, 'RT')], max_length=1),
        ),
    ]
