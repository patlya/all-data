# Generated by Django 3.2.13 on 2022-06-21 06:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0023_rename_students_student_abs'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student_abs',
            options={'ordering': ['st_name']},
        ),
        migrations.AlterModelOptions(
            name='teacher',
            options={'ordering': ['t_name']},
        ),
    ]