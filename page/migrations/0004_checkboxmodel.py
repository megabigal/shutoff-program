# Generated by Django 5.0.7 on 2024-07-19 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0003_remove_logindetails_subway'),
    ]

    operations = [
        migrations.CreateModel(
            name='checkboxModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isChecked', models.BooleanField(default=False)),
            ],
        ),
    ]
