# Generated by Django 2.2.4 on 2019-10-09 03:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_index', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='Content',
            new_name='content',
        ),
    ]
