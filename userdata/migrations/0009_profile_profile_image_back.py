# Generated by Django 5.0.1 on 2024-06-28 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userdata', '0008_profile_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_image_back',
            field=models.ImageField(default=0, upload_to='background/'),
            preserve_default=False,
        ),
    ]
