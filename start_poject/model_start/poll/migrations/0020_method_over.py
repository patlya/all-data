# Generated by Django 3.2.13 on 2022-06-20 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0019_person_dob'),
    ]

    operations = [
        migrations.CreateModel(
            name='method_over',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('dt', models.DateTimeField()),
            ],
        ),
    ]
