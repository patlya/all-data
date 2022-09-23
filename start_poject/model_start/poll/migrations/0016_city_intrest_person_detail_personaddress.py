# Generated by Django 3.2.13 on 2022-06-17 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0015_alter_apply_field_type_field'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Intrest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Person_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.IntegerField()),
                ('intrests', models.ManyToManyField(max_length=200, to='poll.Intrest')),
            ],
        ),
        migrations.CreateModel(
            name='PersonAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_address', models.CharField(max_length=200)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poll.city')),
                ('person', models.OneToOneField(max_length=200, on_delete=django.db.models.deletion.CASCADE, to='poll.person_detail')),
            ],
        ),
    ]