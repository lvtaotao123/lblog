# Generated by Django 2.2.4 on 2019-10-10 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_index', '0003_auto_20191010_1640'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='desc',
            field=models.CharField(max_length=32, null=True),
        ),
    ]
