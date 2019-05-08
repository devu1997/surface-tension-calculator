# Generated by Django 2.0 on 2019-04-23 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SurfaceTension',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('angle', models.IntegerField()),
                ('energy', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='allocate',
            name='asset',
        ),
        migrations.RemoveField(
            model_name='allocate',
            name='task',
        ),
        migrations.RemoveField(
            model_name='allocate',
            name='worker',
        ),
        migrations.DeleteModel(
            name='Allocate',
        ),
        migrations.DeleteModel(
            name='Asset',
        ),
        migrations.DeleteModel(
            name='Task',
        ),
        migrations.DeleteModel(
            name='Worker',
        ),
    ]
