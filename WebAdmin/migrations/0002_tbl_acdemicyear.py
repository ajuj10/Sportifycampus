# Generated by Django 5.0.2 on 2024-04-22 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebAdmin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_acdemicyear',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acdemic_year', models.CharField(max_length=50)),
            ],
        ),
    ]
