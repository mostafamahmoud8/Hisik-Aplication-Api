# Generated by Django 2.1.7 on 2019-04-10 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20190316_0929'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='IP',
        ),
    ]
