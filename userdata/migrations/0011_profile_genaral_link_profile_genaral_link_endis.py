# Generated by Django 5.0.1 on 2024-07-21 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userdata', '0010_profile_google_profile_google_endis_profile_telegram_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='genaral_link',
            field=models.CharField(default=0, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='genaral_link_endis',
            field=models.CharField(default=0, max_length=250),
            preserve_default=False,
        ),
    ]