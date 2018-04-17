# Generated by Django 2.0.4 on 2018-04-17 00:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_auto_20180417_0951'),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
                ('isUsed', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.RenameField(
            model_name='post',
            old_name='writerid',
            new_name='writer_id',
        ),
        migrations.AddField(
            model_name='post',
            name='board_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=250),
        ),
    ]