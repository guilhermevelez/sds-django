# Generated by Django 5.0.2 on 2024-04-07 23:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_building_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='backup',
        ),
        migrations.RemoveField(
            model_name='task',
            name='members',
        ),
        migrations.AlterField(
            model_name='function',
            name='description',
            field=models.TextField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='function',
            name='observations',
            field=models.TextField(max_length=2000),
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('hour_start', models.TimeField()),
                ('hour_end', models.TimeField()),
                ('space', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.space')),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=100)),
                ('internal_id', models.CharField(max_length=30)),
                ('activities', models.ManyToManyField(null=True, to='api.activity')),
            ],
        ),
        migrations.CreateModel(
            name='TaskAssignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_present', models.BooleanField(default=False)),
                ('task_finished', models.BooleanField(default=False)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.member')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.task')),
            ],
        ),
    ]
