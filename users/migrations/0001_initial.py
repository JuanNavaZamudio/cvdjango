# Generated by Django 3.0.5 on 2020-05-05 02:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('addres', models.TextField(max_length=500)),
                ('active', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(max_length=2000)),
                ('save_date', models.DateTimeField(auto_now_add=True)),
                ('topic', models.ManyToManyField(to='users.Topic')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='users.User')),
            ],
        ),
    ]
