# Generated by Django 3.2.8 on 2022-02-21 16:54

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_auto_20220218_1556'),
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, validators=[django.core.validators.RegexValidator(message='Club name must start with a letter and contain only letters, number, and spaces.', regex='^[a-zA-Z][a-zA-Z0-9 ]+')])),
                ('location', models.CharField(max_length=100)),
                ('mission_statement', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
