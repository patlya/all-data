# Generated by Django 3.2.13 on 2022-06-22 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0007_auto_20220622_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='sub_name',
            field=models.ManyToManyField(blank=True, max_length=70, null=True, to='demo.Books'),
        ),
    ]