# Generated by Django 2.2.4 on 2020-11-26 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('user_id', models.IntegerField(blank=True, db_column='id', primary_key=True, serialize=False, unique=True)),
                ('user', models.TextField(blank=True)),
                ('password', models.TextField(blank=True)),
                ('email', models.TextField(blank=True)),
                ('groups', models.TextField(blank=True)),
                ('region', models.TextField(blank=True)),
                ('record', models.TextField(blank=True)),
                ('description', models.TextField(blank=True)),
                ('setting', models.TextField(blank=True)),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.IntegerField(blank=True, db_column='id', primary_key=True, serialize=False, unique=True)),
                ('name', models.TextField(blank=True)),
                ('price', models.IntegerField(blank=True)),
                ('amount', models.IntegerField(blank=True)),
                ('hot', models.IntegerField(blank=True)),
                ('time', models.TextField(blank=True)),
                ('owner', models.TextField(blank=True)),
                ('group', models.TextField(blank=True)),
                ('url', models.TextField(blank=True)),
            ],
            options={
                'db_table': 'product',
            },
        ),
    ]