# Generated by Django 2.1.7 on 2019-03-16 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Role', models.IntegerField()),
                ('Name', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=20)),
                ('IP', models.GenericIPAddressField()),
                ('Email', models.EmailField(max_length=254)),
                ('Token', models.TextField()),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Admin',
                'verbose_name_plural': 'Admins',
            },
        ),
    ]
