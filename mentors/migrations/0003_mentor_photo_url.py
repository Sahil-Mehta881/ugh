# Generated by Django 3.0.6 on 2020-06-12 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentors', '0002_auto_20200612_0129'),
    ]

    operations = [
        migrations.AddField(
            model_name='mentor',
            name='photo_url',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
    ]
