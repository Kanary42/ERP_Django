# Generated by Django 4.1.6 on 2023-02-14 06:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0004_post_parent_delete_subpost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='order_num',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='blog.order'),
        ),
    ]
