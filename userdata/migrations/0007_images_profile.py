# Generated by Django 5.0.1 on 2024-06-25 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userdata', '0006_client_services'),
    ]

    operations = [
        migrations.CreateModel(
            name='images_profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_name', models.CharField(max_length=50)),
                ('profile_image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
