# Generated by Django 3.2.13 on 2022-06-16 12:17

from django.db import migrations, models
import poll.models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0012_alter_animal_z_field'),
    ]

    operations = [
        migrations.CreateModel(
            name='Validation_error',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geeks_mail', models.CharField(max_length=200, validators=[poll.models.Validation_define])),
            ],
        ),
    ]