# Generated by Django 2.2.4 on 2019-10-11 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog_index', '0009_auto_20191011_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='pid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog_index.Comment'),
        ),
    ]
