# Generated by Django 4.1.6 on 2023-02-14 15:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0010_weldmat_alter_control_date_in_alter_control_date_out_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='title',
            field=models.TextField(default='Order'),
        ),
        migrations.AlterField(
            model_name='order',
            name='purchaser',
            field=models.CharField(default='Missing', max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='order_num',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='blog.order'),
        ),
    ]
