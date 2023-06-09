# Generated by Django 4.2.1 on 2023-05-16 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Filiere',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeF', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=10)),
                ('prenom', models.CharField(max_length=10)),
                ('genre', models.CharField(max_length=2)),
                ('email', models.CharField(max_length=20)),
                ('telephone', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Professeur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=10)),
                ('prenom', models.CharField(max_length=10)),
                ('genre', models.CharField(max_length=2)),
                ('email', models.CharField(max_length=20)),
                ('telephone', models.CharField(max_length=15)),
                ('salaire', models.FloatField()),
            ],
        ),
    ]
