# Generated by Django 4.1.7 on 2023-03-15 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dogz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=120)),
                ('raca', models.CharField(max_length=120)),
                ('dono', models.CharField(max_length=120)),
                ('dob', models.TextField(default='blank', max_length=120)),
                ('foto', models.CharField(default='imagepadrao.png', max_length=120)),
                ('obs', models.TextField(default='blank', max_length=120)),
                ('pai', models.TextField(default='blank', max_length=120)),
                ('mae', models.TextField(default='blank', max_length=120)),
                ('site', models.URLField(default='blank', max_length=300)),
            ],
        ),
    ]
