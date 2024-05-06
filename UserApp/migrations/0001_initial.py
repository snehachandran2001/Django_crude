# Generated by Django 5.0.2 on 2024-02-13 05:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DEPARTMENT',
            fields=[
                ('department_id', models.IntegerField(primary_key=True, serialize=False)),
                ('department_name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'department',
            },
        ),
        migrations.CreateModel(
            name='EMPLOY',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employ_name', models.CharField(max_length=255)),
                ('employ_mobile', models.CharField(max_length=255)),
                ('employ_age', models.CharField(max_length=255)),
                ('employ_department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserApp.department')),
            ],
            options={
                'db_table': 'employ_table',
            },
        ),
    ]
