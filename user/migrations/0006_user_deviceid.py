# Generated by Django 2.1.7 on 2019-04-10 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_remove_user_ip'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='DeviceID',
            field=models.CharField(default='', max_length=100),
        ),
    ]