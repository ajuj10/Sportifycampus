# Generated by Django 5.0.2 on 2024-04-22 10:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebAdmin', '0003_tbl_sem'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=30)),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebAdmin.tbl_dept')),
            ],
        ),
    ]
