# Generated by Django 2.2.4 on 2019-10-11 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_index', '0008_auto_20191010_1731'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='article',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
    ]
