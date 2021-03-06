# Generated by Django 2.0 on 2017-12-15 11:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0003_auto_20171215_1721'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='posted_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
