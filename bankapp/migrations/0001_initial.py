# Generated by Django 5.1.3 on 2025-02-28 09:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cust_id', models.CharField(max_length=200)),
                ('fname', models.CharField(max_length=200)),
                ('lname', models.CharField(max_length=200)),
                ('mname', models.CharField(max_length=200)),
                ('address', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('next_of_kin', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_number', models.IntegerField()),
                ('balance', models.FloatField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('holder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankapp.customer')),
            ],
        ),
    ]
