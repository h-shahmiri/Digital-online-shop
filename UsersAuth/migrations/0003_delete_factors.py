# Generated by Django 2.2.6 on 2020-01-23 23:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UsersAuth', '0002_auto_20200123_1213'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Factors',
        ),
    ]