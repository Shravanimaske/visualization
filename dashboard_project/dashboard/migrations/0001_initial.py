# Generated by Django 4.2.4 on 2023-09-12 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataPoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intensity', models.FloatField()),
                ('likelihood', models.FloatField()),
                ('relevance', models.FloatField()),
                ('year', models.IntegerField()),
                ('country', models.CharField(max_length=100)),
                ('topics', models.CharField(max_length=200)),
                ('region', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
            ],
        ),
    ]