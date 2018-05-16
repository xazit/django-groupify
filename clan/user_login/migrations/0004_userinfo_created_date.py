# Generated by Django 2.0.4 on 2018-05-16 09:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user_login', '0003_userinfo_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]