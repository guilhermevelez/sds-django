# Generated by Django 5.0.2 on 2024-04-10 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_task_member_delete_taskassignment'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='activities',
            field=models.ManyToManyField(to='api.activity'),
        ),
        migrations.DeleteModel(
            name='ActivityParticipant',
        ),
    ]
