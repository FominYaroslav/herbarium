# Generated by Django 2.2 on 2020-01-22 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_of_plant', models.CharField(max_length=15)),
                ('name', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30)),
                ('scan', models.ImageField(upload_to='')),
            ],
        ),
    ]
