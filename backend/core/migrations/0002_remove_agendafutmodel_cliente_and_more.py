# Generated by Django 5.0 on 2024-07-30 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agendafutmodel',
            name='cliente',
        ),
        migrations.RemoveField(
            model_name='agendahairmodel',
            name='cliente',
        ),
        migrations.RemoveField(
            model_name='sisorapidomodel',
            name='cliente',
        ),
        migrations.AddField(
            model_name='agendafutmodel',
            name='email',
            field=models.EmailField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='agendafutmodel',
            name='idade',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='agendafutmodel',
            name='nome',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='agendafutmodel',
            name='telefone',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='agendahairmodel',
            name='email',
            field=models.EmailField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='agendahairmodel',
            name='idade',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='agendahairmodel',
            name='nome',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='agendahairmodel',
            name='telefone',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sisorapidomodel',
            name='email',
            field=models.EmailField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='sisorapidomodel',
            name='idade',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sisorapidomodel',
            name='nome',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sisorapidomodel',
            name='telefone',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='clientemodel',
            name='email',
            field=models.EmailField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='clientemodel',
            name='idade',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='clientemodel',
            name='nome',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='clientemodel',
            name='telefone',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
