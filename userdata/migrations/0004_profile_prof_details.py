# Generated by Django 5.0.1 on 2024-06-24 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userdata', '0003_profile_instagram_endis_profile_linkedin_endis_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='prof_details',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
