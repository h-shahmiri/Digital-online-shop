# Generated by Django 2.2.6 on 2020-01-23 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Content', '0001_initial'),
        ('UsersAuth', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Orders',
            new_name='Factors',
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='city_choice',
            field=models.CharField(choices=[('Tehran', 'tehran'), ('Soon', 'soon')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='state_choice',
            field=models.CharField(choices=[('Tehran', 'tehran'), ('Soon', 'soon')], max_length=50, null=True),
        ),
    ]