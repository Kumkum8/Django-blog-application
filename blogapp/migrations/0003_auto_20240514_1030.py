# Generated by Django 3.2.25 on 2024-05-14 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_post_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='status',
        ),
        migrations.RemoveField(
            model_name='post',
            name='updated_on',
        ),
    ]
