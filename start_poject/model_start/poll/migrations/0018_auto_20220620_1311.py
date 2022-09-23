# Generated by Django 3.2.13 on 2022-06-20 07:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0017_author_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group_through',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Person_through',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_query_name='book', to='poll.author'),
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateField()),
                ('invite_reason', models.CharField(max_length=200)),
                ('group', models.ForeignKey(max_length=200, on_delete=django.db.models.deletion.CASCADE, to='poll.group_through')),
                ('person', models.ForeignKey(max_length=200, on_delete=django.db.models.deletion.CASCADE, to='poll.person_through')),
            ],
        ),
        migrations.AddField(
            model_name='group_through',
            name='members',
            field=models.ManyToManyField(through='poll.Membership', to='poll.Person_through'),
        ),
    ]