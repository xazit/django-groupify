# Generated by Django 2.0.4 on 2018-05-17 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_login', '0004_userinfo_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_picture/'),
        ),
    ]
