# Generated by Django 2.2.4 on 2019-10-10 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_index', '0005_auto_20191010_1723'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='IndexLinks',
            new_name='Indexlink',
        ),
    ]