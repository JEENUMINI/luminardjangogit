# Generated by Django 3.1.3 on 2020-11-17 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_name', models.CharField(max_length=150, unique=True)),
                ('age', models.IntegerField()),
                ('salary', models.IntegerField()),
                ('designation', models.CharField(max_length=120)),
            ],
        ),
    ]
