# Generated by Django 5.0.3 on 2024-04-05 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_agenda_email_alter_agenda_n_cll'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='data',
            field=models.CharField(max_length=80),
        ),
    ]