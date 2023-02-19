# Generated by Django 4.1.6 on 2023-02-19 10:36

import blog.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChemicalComposition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ccfile', models.FileField(upload_to=blog.models.content_file_name)),
            ],
        ),
        migrations.CreateModel(
            name='ControlInput',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_in', models.DateField(default=django.utils.timezone.now)),
                ('is_accepted_in', models.BooleanField()),
                ('in_file', models.FileField(upload_to=blog.models.content_file_name)),
            ],
        ),
        migrations.CreateModel(
            name='ControlOutput',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_out', models.DateField(default=django.utils.timezone.now)),
                ('is_accepted_out', models.BooleanField()),
                ('out_file', models.FileField(upload_to=blog.models.content_file_name)),
            ],
        ),
        migrations.CreateModel(
            name='PenetrantTesting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ptfile', models.ImageField(upload_to=blog.models.content_file_name)),
            ],
        ),
        migrations.RemoveField(
            model_name='order',
            name='order_num',
        ),
        migrations.AddField(
            model_name='post',
            name='date_added',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='post',
            name='deadline',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='serial_num',
            field=models.CharField(default='Missing', max_length=100),
        ),
        migrations.AlterField(
            model_name='ingress',
            name='order_num',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.post'),
        ),
        migrations.AlterField(
            model_name='weldmaterialuse',
            name='order_num',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.post'),
        ),
        migrations.DeleteModel(
            name='Control',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.AddField(
            model_name='penetranttesting',
            name='order_num',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.post'),
        ),
        migrations.AddField(
            model_name='controloutput',
            name='order_num',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.post'),
        ),
        migrations.AddField(
            model_name='controlinput',
            name='order_num',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.post'),
        ),
        migrations.AddField(
            model_name='chemicalcomposition',
            name='order_num',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.post'),
        ),
    ]
