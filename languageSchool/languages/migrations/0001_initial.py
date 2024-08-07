# Generated by Django 5.0.7 on 2024-07-19 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_name', models.CharField(max_length=250)),
                ('language_family', models.CharField(max_length=250)),
                ('region_origin', models.CharField(max_length=250)),
                ('sentences', models.TextField()),
                ('words', models.TextField()),
            ],
        ),
    ]
