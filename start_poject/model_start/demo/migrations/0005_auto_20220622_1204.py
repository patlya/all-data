# Generated by Django 3.2.13 on 2022-06-22 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0004_auto_20220622_1154'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='tec_name',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='sub_name',
        ),
        migrations.AddField(
            model_name='teacher',
            name='sub_name',
            field=models.ManyToManyField(max_length=70, to='demo.Books'),
        ),
    ]
