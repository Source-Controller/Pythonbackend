# Generated by Django 2.1.5 on 2021-06-27 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0002_down_vote_total_view'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='question',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
