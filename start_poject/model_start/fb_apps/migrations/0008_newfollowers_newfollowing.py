# Generated by Django 3.2.13 on 2022-06-29 11:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fb_apps', '0007_auto_20220629_1635'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewFollowing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('following_user_name', models.ManyToManyField(blank=True, null=True, related_name='following', to=settings.AUTH_USER_MODEL)),
                ('usr_follwing', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_following', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='NewFollowers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follow_user_id', models.ManyToManyField(blank=True, null=True, related_name='follower', to=settings.AUTH_USER_MODEL)),
                ('usr_follrs', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='usr_follrs', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
