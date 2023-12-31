# Generated by Django 4.2.2 on 2023-06-22 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('memoire', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Taches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('dateDebut', models.DateField()),
                ('dateFin', models.DateField()),
                ('projet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='memoire.project')),
            ],
        ),
    ]
