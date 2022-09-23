# Generated by Django 3.2.13 on 2022-07-11 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0025_alter_student_abs_managers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_name', models.CharField(blank=True, max_length=200, null=True)),
                ('total_marks', models.IntegerField()),
                ('obtain_mark', models.IntegerField()),
            ],
        ),
    ]