# Generated by Django 2.2 on 2020-08-04 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_auto_20200504_0155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='country',
            field=models.CharField(choices=[('Slovensko', 'Slovakia'), ('Cesko', 'Czechia'), ('Rakusko', 'Austria'), ('Polsko', 'Poland'), ('Nemecko', 'Germany')], default=('Slovensko', 'Slovakia'), max_length=30),
        ),
    ]